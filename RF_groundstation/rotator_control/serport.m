%T = readtable('data.xls', 'Sheet',1, 'Range','A2:B10')



function [outputArg1] = serport(~,~,~)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
filename='data.xlsx'; %Name of file
x=xlsread(filename, 'B2:B2');
y=xlsread(filename, 'C2:C2');
z=xlsread(filename, 'D2:D2');
%position = lla2eci([5 -75 1000],[2010 1 17 10 20 36]);
%ber = eci2aer([x ,y, z],...
%[1969,7,20,21,17,40], [42.444,-76.5019,50]);
ber = eci2aer([x ,y, z],...
[1969,7,20,21,17,40], [42.444,-76.5019,50]);
%der = eci2aer(lla2eci([5 -75 1000],[2010 1 17 10 20 36]), [1969,7,20,21,17,40], [28.4,-80.5,2.7], 'dCIP',[-0.2530e-6 -0.0188e-6]);
if ~isempty(instrfind)
    fclose(instrfind);
    delete(instrfind);
end
s = serial('COM3');
set(s,'BaudRate',9600); %choose later
fopen(s);
%ber = [20, 10];

az = ber(1,1);
el = ber(1,2);
az = 10*(360+az);
el=10*(360+el);
azhun = (az-mod(az,100))/100;
azten = (az-azhun*100-mod(az,10))/10;
azone = (az-azhun*100-azten*10-mod(az,1));
azdec = mod(az,1);
elhun = (el-mod(el,100))/100;
elten = (el-azhun*100-mod(el,10))/10;
elone = (el-elhun*100-elten*10-mod(el,1));  
eldec = mod(el,1);
%j = 10
%inbinary = ['W',int2str(48),int2str(57),int2str(54),int2str(55),int2str(2),int2str(48),int2str(56),int2str(55),int2str(52),int2str(2),int2str(47),int2str(32)];
%disp(inbinary);
disp(char(47));
inbinary = 'W0967'+char(10)+'0874' + char(10)+char(47)+char(32);
%instring = ['57','30','39','36','37','02','30','38','37','34','02','2F','20'];
%instring = ['57','30',num2str(30+azhun),num2str(30+azten),num2str(30+azone),'02','30',num2str(30+elhun),num2str(30+elten),num2str(30+elone),'02','2F','20'];
%inbinary = hex2dec(instring);
%disp(inbinary);
fwrite(s,inbinary);
%'%s%s%s%s%s%s%s%s%s%s%s%s%s',['87',azhun,azten,azone,azdec,0,elhun,elten,elone,eldec,'2','47','32'
%fprintf(s,instring);
%out = fscanf(s);
fclose(s);
delete(s);
clear s
successs = ber(1, 1);
outputArg1 = successs;


end

