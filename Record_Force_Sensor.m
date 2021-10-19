%Written by Kenneth Cheung on 2/27/21
%This script records from the load cell for a user-specificed amount of
%time and then plots the data.

%USER WARNING:  Do NOT apply load in first second after the script is run.
%The average of the raw voltages in the first second is used to zero the
%sensor.

t=10; %Data record duration (sec), a user input

d=daqlist("ni"); %Listing all detected DAQ devices
dq = daq("ni");
dq.Rate = 10000; %in hertz
NBR = 350; %Nominal bridge resistance, value from heritage code
VR = [0.0216277954	0.02144604827	0.02231647519	0.01961606674	0.02168339645	0.01911262775];
EV = 5; %Strain gauge excitation voltage, value from heritage code

%Setting up the NI9237 cards in slots 1 and 2 as bridge inputs:
Strain_D1 = dq.addinput('cDAQ1Mod1',(1:4) - 1,'Bridge');
Strain_D2 = dq.addinput('cDAQ1Mod2',(1:2) - 1,'Bridge');
Strain_D1(1).ExcitationSource = 'External';
Strain_D2(1).ExcitationSource = 'External'; 
set(Strain_D1, 'BridgeMode', 'Half');                                   
set(Strain_D2, 'BridgeMode', 'Half');
set(Strain_D1, 'NominalBridgeResistance', NBR);                    
set(Strain_D2, 'NominalBridgeResistance', NBR);
set(Strain_D1, 'ExcitationVoltage', EV);                           
set(Strain_D2, 'ExcitationVoltage', EV);
set(Strain_D1(1,1), 'Range', VR(1).*[-1 1]);   
set(Strain_D1(1,2), 'Range', VR(2).*[-1 1]);  
set(Strain_D1(1,3), 'Range', VR(3).*[-1 1]);  
set(Strain_D1(1,4), 'Range', VR(4).*[-1 1]);  
set(Strain_D2(1,1), 'Range', VR(5).*[-1 1]);
set(Strain_D2(1,2), 'Range', VR(6).*[-1 1]);

%Record data for t seconds:
rawdata=read(dq, seconds(t));

%Converting to a numerical array:
data=(timetable2table(rawdata));
data=table2array(data(:,2:end));

%Matrix from cablibration sheet
calibrationMatrix=[-1.61804949	-1.872014423	17.56060715	-791.477083	-14.48275848	809.3501008
-64.90265717	913.3995385	14.08262677	-480.6927557	12.00735328	-454.6883466
815.247046	11.96348149	829.625717	7.258125609	839.6956121	-9.301521904
-417.9246673	5525.364151	4632.440105	-2856.719421	-4593.264791	-2733.250305
-5178.954691	-52.52785919	2671.778191	4798.725591	2733.089921	-4926.605752
-181.9479067	3205.374752	-82.925508	3212.797379	-91.61386068	3591.398831];

%Experimentally determined correction factor
correctionFactor=4.43665625201744/.531045;

 %Offset vector for zeroing the strain gauges.  Uses average of readings
 %for the first second of data:
offsetVector=mean(data(1:10000,:));

%Preallocating processed data matrix:
[nr, nc, ~]=size(data);
processedData=ones(nr,nc); 

%Filtering out high-frequency noise:
data(:,1) = lowpass(data(:,1),1000,dq.Rate);
data(:,2) = lowpass(data(:,2),1000,dq.Rate);
data(:,3) = lowpass(data(:,3),1000,dq.Rate);
data(:,4) = lowpass(data(:,4),1000,dq.Rate);
data(:,5) = lowpass(data(:,5),1000,dq.Rate);
data(:,6) = lowpass(data(:,6),1000,dq.Rate);

%Postprocessing by subtracting each reading with the offset vector and then
%post-multiplying with the calibration matrix:
for i=1:nr
    currentData=data(i,:);
    offsetCorrectedData=currentData-offsetVector;
    processedData(i,:)=correctionFactor*(calibrationMatrix*offsetCorrectedData')';
end




%Plot raw voltages:
figure(1)
plot(rawdata.Time, rawdata.Variables);
ylabel("Voltage (V)")
xlabel("Time (sec)")
legend("V0","V1","V2","V3","V4","V5");
title("Raw Voltages vs. Time")
grid on
box on

%Plot processed data:
figure(2)
plot(rawdata.Time, processedData);
ylabel("Force (N), Moment (N*mm)")
xlabel("Time (sec)")
legend("Fx","Fy","Fz","Mx","My","Mz");
title("Force/Moment vs. Time")
grid on
box on
