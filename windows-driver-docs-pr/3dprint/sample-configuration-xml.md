---
title: Sample configuration XML
description: Use the sample configuration XML in this topic to develop configuration files for your device.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sample configuration XML

You can use the following example configuration XML to develop the configuration files for your device.

```xml
<?xml version="1.0"?>
<PrintDeviceCapabilities
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:xml="http://www.w3.org/XML/1998/namespace"
    xmlns:psk="http://schemas.microsoft.com/windows/2003/08/printing/printschemakeywords"
    xmlns:psk3d="http://schemas.microsoft.com/3dmanufacturing/2013/01/pskeywords3d"
    xmlns:psk3dx="http://schemas.microsoft.com/3dmanufacturing/2014/11/pskeywords3dextended"
    xmlns:pskv="http://schemas.microsoft.com/3dmanufacturing/2014/11/pskeywordsvendor"
    xmlns:psf="http://schemas.microsoft.com/windows/2003/08/printing/printschemaframework"
    xmlns:psf2="http://schemas.microsoft.com/windows/2013/12/printing/printschemaframework2"
    xmlns="http://schemas.microsoft.com/windows/2013/12/printing/printschemaframework2"
    version="2">
    <CapabilitiesChangeID xsi:type="xsd:string">{9F58AF07-DCB6-4865-8CA3-A52EA5DCB05F}</CapabilitiesChangeID>

  <psk3d:Job3DOutputArea psf2:psftype="Property">
    <psk3d:Job3DOutputAreaWidth>254001</psk3d:Job3DOutputAreaWidth>
    <psk3d:Job3DOutputAreaDepth>254001</psk3d:Job3DOutputAreaDepth>
    <psk3d:Job3DOutputAreaHeight>254001</psk3d:Job3DOutputAreaHeight>

    <psk3dx:Job3DOutputAreaOffsetX>0</psk3dx:Job3DOutputAreaOffsetX>
    <psk3dx:Job3DOutputAreaOffsetY>0</psk3dx:Job3DOutputAreaOffsetY>

    <psk3dx:autocenter>0</psk3dx:autocenter>

  </psk3d:Job3DOutputArea>

  <psk3d:Job3DMaterials psf2:psftype="Property">

      <!-- Material entries --> 
      <psk3dx:extruders>2</psk3dx:extruders>

      <psk3dx:MaterialPLA>
         <psk:DisplayName>PLA</psk:DisplayName>
         <psk3d:Job3DMaterialType>psk3d:PLA</psk3d:Job3DMaterialType>
         <psk3d:MaterialColor>#FFFFFFFF</psk3d:MaterialColor>

         <psk3dx:platformtemperature>0</psk3dx:platformtemperature>
         <psk3dx:filamentdiameter>1750</psk3dx:filamentdiameter>
         <psk3dx:filamentcalibrationoverride>1.0</psk3dx:filamentcalibrationoverride>
         <psk3dx:extrudertemperature>207</psk3dx:extrudertemperature>

         <psk3dx:SpeedFactor>1.0</psk3dx:SpeedFactor>

         <psk3dx:SetupCommands>
            <!-- Executed during pre-commands: nozzle pre-heating, priming, etc --> 
            <psk3dx:command>T0</psk3dx:command>
            <psk3dx:command>M104 S$extrudertemperature$</psk3dx:command>
         </psk3dx:SetupCommands>

         <psk3dx:SelectCommands>
            <!-- Executed during printing: T0/T1 selection, nozzle wiping sequence,turn fan on/off/gradual, retract the material, temperature, etc--> 
            <psk3dx:command>; PLA on</psk3dx:command>
            <psk3dx:command>T0</psk3dx:command>
         </psk3dx:SelectCommands>

         <psk3dx:DeselectCommands>
            <!-- Executed during printing: retract the material, park the nozzle, reduce temperature, etc --> 
            <psk3dx:command>; PLA off</psk3dx:command>
         </psk3dx:DeselectCommands>


      </psk3dx:MaterialPLA>

      <psk3dx:MaterialABS>
         <psk:DisplayName>ABS</psk:DisplayName>
         <psk3d:Job3DMaterialType>psk3d:PLA</psk3d:Job3DMaterialType>
         <psk3d:MaterialColor>#208040FF</psk3d:MaterialColor>

         <psk3dx:platformtemperature>0</psk3dx:platformtemperature>
         <psk3dx:filamentdiameter>1750</psk3dx:filamentdiameter>
         <psk3dx:filamentcalibrationoverride>1.0</psk3dx:filamentcalibrationoverride>
         <psk3dx:extrudertemperature>207</psk3dx:extrudertemperature>

         <psk3dx:SpeedFactor>1.0</psk3dx:SpeedFactor>

         <psk3dx:SetupCommands>
            <!-- Executed during pre-commands: nozzle pre-heating, priming, etc --> 
            <psk3dx:command>T1</psk3dx:command>
            <psk3dx:command>M104 S$extrudertemperature$</psk3dx:command>
         </psk3dx:SetupCommands>

         <psk3dx:SelectCommands>
            <!-- Executed during printing: T0/T1 selection, nozzle wiping sequence,turn fan on/off/gradual, retract the material, temperature, etc--> 
            <psk3dx:command>; ABS on</psk3dx:command>
            <psk3dx:command>T1</psk3dx:command>
         </psk3dx:SelectCommands>

         <psk3dx:DeselectCommands>
            <!-- Executed during printing: retract the material, park the nozzle, reduce temperature, etc --> 
            <psk3dx:command>; ABS off</psk3dx:command>
         </psk3dx:DeselectCommands>

      </psk3dx:MaterialABS>

      <psk3dx:MaterialFlexible>
         <psk:DisplayName>Flexible</psk:DisplayName>
         <psk3d:Job3DMaterialType>psk3d:PLA</psk3d:Job3DMaterialType>
         <psk3d:MaterialColor>#FF80FFFF</psk3d:MaterialColor>

         <psk3dx:platformtemperature>0</psk3dx:platformtemperature>
         <psk3dx:filamentdiameter>1750</psk3dx:filamentdiameter>
         <psk3dx:filamentcalibrationoverride>1.0</psk3dx:filamentcalibrationoverride>
         <psk3dx:extrudertemperature>207</psk3dx:extrudertemperature>

         <psk3dx:SpeedFactor>1.0</psk3dx:SpeedFactor>

         <psk3dx:SetupCommands>
            <!-- Executed during pre-commands: nozzle pre-heating, priming, etc --> 
            <psk3dx:command>T0</psk3dx:command>
            <psk3dx:command>M104 S$extrudertemperature$</psk3dx:command>
         </psk3dx:SetupCommands>

         <psk3dx:SelectCommands>
            <!-- Executed during printing: T0/T1 selection, nozzle wiping sequence,turn fan on/off/gradual, retract the material, temperature, etc--> 
            <psk3dx:command>; Flexible on</psk3dx:command>
            <psk3dx:command>T0</psk3dx:command>
         </psk3dx:SelectCommands>

         <psk3dx:DeselectCommands>
            <!-- Executed during printing: retract the material, park the nozzle, reduce temperature, etc --> 
            <psk3dx:command>; Flexible off</psk3dx:command>
         </psk3dx:DeselectCommands>

      </psk3dx:MaterialFlexible>


  </psk3d:Job3DMaterials>

  <psk3dx:customStatus>Slicing</psk3dx:customStatus>
  <psk3dx:userprompt>Confirm the 3D printer is calibrated and ready for the next print</psk3dx:userprompt>

  <psk3dx:MS3DPrinter>

      <!-- 
        <psk3dx:debug>
          <psk3dx:log>c:\windows\temp\3DPrint\StandardGCode.log</psk3dx:log>
        </psk3dx:debug>
      -->  

      <psk3dx:communication>
        <!-- communication parameters -->
        <psk3dx:connection name="serialport">
          <psk3dx:comport></psk3dx:comport> <!-- leave empty for PnP or specify a file URI -->
          <psk3dx:baudrate>115200</psk3dx:baudrate>
          <psk3dx:mode>0</psk3dx:mode>
          <psk3dx:timeout>0</psk3dx:timeout>
        </psk3dx:connection>
      </psk3dx:communication>

      <psk3dx:customcommands>

        <!-- Commands sent before slicing -->
        <psk3dx:initcommands>
          <psk3dx:command>M110 N0</psk3dx:command> <!-- Reset line numbers -->
          <psk3dx:command>G28</psk3dx:command> <!-- Home  -->
          <psk3dx:command>G0 X75 Y150 Z10</psk3dx:command> <!-- Go to a safe position above the bed -->
          <psk3dx:command>M104 S175</psk3dx:command> <!-- pre-heat while slicing but prevent ooze -->
        </psk3dx:initcommands>

        <!-- Commands sent at the beginning of print -->
        <psk3dx:precommands>
          <psk3dx:command>M110 N0</psk3dx:command> <!-- Reset line numbers -->
          <psk3dx:command>T0</psk3dx:command> <!-- Default to primary extruder -->
          <psk3dx:command>M104 S$extrudertemperature$</psk3dx:command> <!-- Set extruder temperature -->
          <psk3dx:command>M140 S$platformtemperature$</psk3dx:command> <!-- Set bed temperature -->
          <psk3dx:command>G90</psk3dx:command> <!-- Set axis to absolute -->
          <psk3dx:command>M82</psk3dx:command> <!-- Set extruder to absolute -->
          <psk3dx:command>G28</psk3dx:command> <!-- Home -->
          <psk3dx:command>G1 X75 Y150 Z15 F4000</psk3dx:command> <!-- Move above the bed -->
          <psk3dx:command>M109 S$extrudertemperature$</psk3dx:command> <!-- Go to temperature -->
          <psk3dx:command>M190 S$platformtemperature$</psk3dx:command> <!-- Go to temperature -->          
          <psk3dx:command>M106 S$rampup$</psk3dx:command> <!-- Start the fan -->
          <psk3dx:command>G28 X Y</psk3dx:command> <!-- Home -->
          <psk3dx:command>G29</psk3dx:command> <!-- Auto-leveling -->
          <psk3dx:command>G92 E0</psk3dx:command> <!-- Reset E axis -->
          <psk3dx:command>G1 X-2 Y151 Z0.25 F10000</psk3dx:command>
          <psk3dx:command>G1 X-2 Y0 Z0.25 E20.0 F2000</psk3dx:command> <!-- prime the nozzle -->
          <psk3dx:command>G1 X-2 Y0 Z0.25 E19.0 F4000</psk3dx:command> <!-- retract -->
          <psk3dx:command>G1 X-1 Y75 F8000</psk3dx:command>
          <psk3dx:command>G1 X5 Y75 F8000</psk3dx:command>
          <psk3dx:command>G1 X-2 Y75 F8000</psk3dx:command>
          <psk3dx:command>G1 X5 Y75 F8000</psk3dx:command>
          <psk3dx:command>G92 E-1.0</psk3dx:command> <!-- Start retracted -->
        </psk3dx:precommands>

        <!-- Commands sent at the end of print -->
        <psk3dx:postcommands>
          <psk3dx:command>M110 N0</psk3dx:command>
          <psk3dx:command>G92 E0</psk3dx:command> <!-- Reset E axis -->
          <psk3dx:command>G1 E-0.5 F3600</psk3dx:command> <!-- Retract to prevent last blob -->
          <psk3dx:command>M104 S0</psk3dx:command> <!-- Turn off extruder -->
          <psk3dx:command>M140 S0</psk3dx:command><!-- Turn off heated bed -->
          <psk3dx:command>G1 X0 Y150 F10000</psk3dx:command> <!-- Move out of the way -->
          <psk3dx:command>G91 Z</psk3dx:command> <!-- move Z to relative -->
          <psk3dx:command>G0 Z15</psk3dx:command> <!-- move Z to relative -->
          <psk3dx:command>G90</psk3dx:command> <!-- switch back to absolute coordinates -->
          <psk3dx:command>M106 S0</psk3dx:command>  <!-- Turn off the fan -->
          <psk3dx:command>M18</psk3dx:command> <!-- Turn off motors, same as M84 -->
        </psk3dx:postcommands>

        <!-- Commands sent just in case for safety -->
        <psk3dx:failsafepostcommands>
          <psk3dx:command>M140 S0</psk3dx:command><!-- Turn off extruder -->
          <psk3dx:command>M140 S0</psk3dx:command><!-- Turn off heated bed -->
          <psk3dx:command>M104 S0</psk3dx:command> <!-- Turn off extruder -->
        </psk3dx:failsafepostcommands>

        <!-- Commands sent between layers -->
        <psk3dx:layer>
          <psk3dx:command>M106 S$rampup$</psk3dx:command>
        </psk3dx:layer>

      </psk3dx:customcommands>

      <psk3dx:print>
        <psk3dx:medium default="true"> <!-- model parameters -->
          <psk3dx:layerthickness>250</psk3dx:layerthickness> <!-- layer thickness (micron) -->
          <psk3dx:maxlayerthickness>500</psk3dx:maxlayerthickness><!-- maximum  layer thickness (micron) -->
          <psk3dx:minlayerthickness>100</psk3dx:minlayerthickness><!-- minimum layer thickness (micron) -->
          <psk3dx:pathwidth>400</psk3dx:pathwidth> <!-- path width (micron) -->
          <psk3dx:shells>3</psk3dx:shells> <!-- number of perimeters (zero would make the infill visible) -->
          <psk3dx:shelloffset>0</psk3dx:shelloffset><!-- offset of the shells (micron) -->
          <psk3dx:topsurfacelayers>4</psk3dx:topsurfacelayers> <!-- number of solid top surface layers -->
          <psk3dx:bottomsurfacelayers>4</psk3dx:bottomsurfacelayers> <!-- number of solid bottom surface layers -->
          <psk3dx:filllow>0.15</psk3dx:filllow> <!-- low density sparse infill fraction (between 0 and 1, inclusive) -->
          <psk3dx:fillmedium>0.25</psk3dx:fillmedium> <!-- medium density sparse infill fraction (between 0 and 1, inclusive) -->
          <psk3dx:fillhigh>0.40</psk3dx:fillhigh> <!-- high density sparse infill fraction (between 0 and 1, inclusive) -->
          <psk3dx:fillangle>45</psk3dx:fillangle> <!-- intial fill angle (degrees) -->
          <psk3dx:filloverlap>0.15</psk3dx:filloverlap> <!-- infill overlap (between 0 and 1 of the path width, inclusive) -->
          <psk3dx:speed>75000</psk3dx:speed> <!-- speed of normal printing movements (micron/s) -->
          <psk3dx:speedouter>45000</psk3dx:speedouter> <!-- speed of outer perimeter (micron/s) -->
          <psk3dx:speedfirst>20000</psk3dx:speedfirst> <!-- speed of first layer (micron/s), supercedes speedOuter -->
          <psk3dx:speedtravel>120000</psk3dx:speedtravel> <!-- speed of non-extrusion moves (micron/s) -->
          <psk3dx:speedretract>35000</psk3dx:speedretract> <!-- speed of filament retraction (micron/s) -->
          <psk3dx:retraction>1500</psk3dx:retraction> <!-- amount of retraction (micron) -->
          <psk3dx:supportorientationoptimization>0</psk3dx:supportorientationoptimization> <!-- Apply the best orientation -->
          <psk3dx:supportoverhangangle>45</psk3dx:supportoverhangangle> <!-- The minimum overhang angle to generate support -->
          <psk3dx:supportzgap>350</psk3dx:supportzgap> <!-- The Z gap in micron -->
          <psk3dx:supportxygap>400</psk3dx:supportxygap> <!-- The XY gap in micron -->
          <psk3dx:supportfill>0.2</psk3dx:supportfill> <!-- sparse infill fraction for support (between 0 and 1, inclusive) -->
          <psk3dx:raftlayers>2</psk3dx:raftlayers><!-- number of solid raft layers -->
          <psk3dx:raftlayerthickness>600</psk3dx:raftlayerthickness><!-- layer thickness of the raft (micron) -->
          <psk3dx:raftpathwidth>2000</psk3dx:raftpathwidth><!-- path width of raft (micron) -->
          <psk3dx:raftfill>0.6</psk3dx:raftfill><!-- sparse infill fraction for support (between 0 and 1, inclusive) -->
          <psk3dx:raftoffset>2000</psk3dx:raftoffset><!-- size of the raft (micron) -->
          <psk3dx:raftzgap>350</psk3dx:raftzgap><!-- The Z gap (micron) -->
          <psk3dx:raftspeedfirst>20000</psk3dx:raftspeedfirst> <!-- speed of raft first layer (micron/s) -->
          <psk3dx:coolingtime>5</psk3dx:coolingtime><!-- cooling time for a layer (second) -->
          <psk3dx:rampuptarget>500</psk3dx:rampuptarget> <!-- Z target for the fan to run at full speed -->
          <psk3dx:mincoolingspeed>1000</psk3dx:mincoolingspeed><!-- the minimum cooling speed for a layer (micron/s) -->
          <psk3dx:bridgingspeed>10000</psk3dx:bridgingspeed><!-- the speed for bridging (micron/s) -->
        </psk3dx:medium>
        <psk3dx:high default="false"> <!-- model parameters -->
          <psk3dx:layerthickness>150</psk3dx:layerthickness> <!-- layer thickness (micron) -->
          <psk3dx:maxlayerthickness>500</psk3dx:maxlayerthickness><!-- maximum  layer thickness (micron) -->
          <psk3dx:minlayerthickness>100</psk3dx:minlayerthickness><!-- minimum layer thickness (micron) -->
          <psk3dx:pathwidth>400</psk3dx:pathwidth> <!-- path width (micron) -->
          <psk3dx:shells>3</psk3dx:shells> <!-- number of perimeters (zero would make the infill visible) -->
          <psk3dx:shelloffset>50</psk3dx:shelloffset><!-- offset of the shells (micron) -->
          <psk3dx:topsurfacelayers>4</psk3dx:topsurfacelayers> <!-- number of solid top surface layers -->
          <psk3dx:bottomsurfacelayers>4</psk3dx:bottomsurfacelayers> <!-- number of solid bottom surface layers -->
          <psk3dx:filllow>0.15</psk3dx:filllow> <!-- low density sparse infill fraction (between 0 and 1, inclusive) -->
          <psk3dx:fillmedium>0.30</psk3dx:fillmedium> <!-- medium density sparse infill fraction (between 0 and 1, inclusive) -->
          <psk3dx:fillhigh>0.45</psk3dx:fillhigh> <!-- high density sparse infill fraction (between 0 and 1, inclusive) -->
          <psk3dx:fillangle>45</psk3dx:fillangle> <!-- intial fill angle (degrees) -->
          <psk3dx:filloverlap>0.15</psk3dx:filloverlap> <!-- infill overlap (between 0 and 1 of the path width, inclusive) -->
          <psk3dx:speed>70000</psk3dx:speed> <!-- speed of normal printing movements (micron/s) -->
          <psk3dx:speedouter>30000</psk3dx:speedouter> <!-- speed of outer perimeter (micron/s) -->
          <psk3dx:speedfirst>20000</psk3dx:speedfirst> <!-- speed of first layer (micron/s), supercedes speedOuter -->
          <psk3dx:speedtravel>120000</psk3dx:speedtravel> <!-- speed of non-extrusion moves (micron/s) -->
          <psk3dx:supportorientationoptimization>0</psk3dx:supportorientationoptimization> <!-- Apply the best orientation -->
          <psk3dx:supportoverhangangle>45</psk3dx:supportoverhangangle> <!-- The minimum overhang angle to generate support -->
          <psk3dx:supportzgap>350</psk3dx:supportzgap> <!-- The Z gap in micron -->
          <psk3dx:supportxygap>400</psk3dx:supportxygap> <!-- The XY gap in micron -->
          <psk3dx:supportfill>0.2</psk3dx:supportfill> <!-- sparse infill fraction for support (between 0 and 1, inclusive) -->
          <psk3dx:raftlayers>2</psk3dx:raftlayers><!-- number of solid raft layers -->
          <psk3dx:raftlayerthickness>600</psk3dx:raftlayerthickness><!-- layer thickness of the raft (micron) -->
          <psk3dx:raftpathwidth>2000</psk3dx:raftpathwidth><!-- path width of raft (micron) -->
          <psk3dx:raftfill>0.6</psk3dx:raftfill><!-- sparse infill fraction for support (between 0 and 1, inclusive) -->
          <psk3dx:raftoffset>2000</psk3dx:raftoffset><!-- size of the raft (micron) -->
          <psk3dx:raftzgap>350</psk3dx:raftzgap><!-- The Z gap (micron) -->
          <psk3dx:raftspeedfirst>20000</psk3dx:raftspeedfirst> <!-- speed of raft first layer (micron/s) -->
          <psk3dx:coolingtime>5</psk3dx:coolingtime><!-- cooling time for a layer (second) -->
          <psk3dx:rampuptarget>500</psk3dx:rampuptarget> <!-- Z target for the fan to run at full speed -->
          <psk3dx:mincoolingspeed>1000</psk3dx:mincoolingspeed><!-- the minimum cooling speed for a layer (micron/s) -->
          <psk3dx:bridgingspeed>10000</psk3dx:bridgingspeed><!-- the speed for bridging (micron/s) -->
        </psk3dx:high>
        <psk3dx:draft default="false"><!-- model parameters -->
          <psk3dx:layerthickness>350</psk3dx:layerthickness><!-- layer thickness (micron) -->
          <psk3dx:maxlayerthickness>500</psk3dx:maxlayerthickness><!-- maximum  layer thickness (micron) -->
          <psk3dx:minlayerthickness>100</psk3dx:minlayerthickness><!-- minimum layer thickness (micron) -->
          <psk3dx:pathwidth>560</psk3dx:pathwidth><!-- path width (micron) -->
          <psk3dx:shells>2</psk3dx:shells><!-- number of perimeters (zero would make the infill visible) -->
          <psk3dx:shelloffset>50</psk3dx:shelloffset><!-- offset of the shells (micron) -->
          <psk3dx:topsurfacelayers>4</psk3dx:topsurfacelayers><!-- number of solid top surface layers -->
          <psk3dx:bottomsurfacelayers>4</psk3dx:bottomsurfacelayers><!-- number of solid bottom surface layers -->
          <psk3dx:filllow>0.10</psk3dx:filllow> <!-- low density sparse infill fraction (between 0 and 1, inclusive) -->
          <psk3dx:fillmedium>0.20</psk3dx:fillmedium> <!-- medium density sparse infill fraction (between 0 and 1, inclusive) -->
          <psk3dx:fillhigh>0.35</psk3dx:fillhigh> <!-- high density sparse infill fraction (between 0 and 1, inclusive) -->
          <psk3dx:fillangle>45</psk3dx:fillangle><!-- intial fill angle (degrees) -->
          <psk3dx:filloverlap>0.15</psk3dx:filloverlap><!-- infill overlap (between 0 and 1 of the path width, inclusive) -->
          <psk3dx:speed>100000</psk3dx:speed><!-- speed of normal printing movements (micron/s) -->
          <psk3dx:speedouter>100000</psk3dx:speedouter><!-- speed of outer perimeter (micron/s) -->
          <psk3dx:speedfirst>30000</psk3dx:speedfirst><!-- speed of first layer (micron/s), supercedes speedOuter -->
          <psk3dx:speedtravel>150000</psk3dx:speedtravel><!-- speed of non-extrusion moves (micron/s) -->
          <psk3dx:speedretract>40000</psk3dx:speedretract><!-- speed of filament retraction (micron/s) -->
          <psk3dx:retraction>1500</psk3dx:retraction><!-- amount of retraction (micron) -->
          <psk3dx:supportorientationoptimization>0</psk3dx:supportorientationoptimization><!-- Apply the best orientation -->
          <psk3dx:supportoverhangangle>45</psk3dx:supportoverhangangle><!-- The minimum overhang angle to generate support -->
          <psk3dx:supportzgap>500</psk3dx:supportzgap><!-- The Z gap in micron -->
          <psk3dx:supportxygap>560</psk3dx:supportxygap><!-- The XY gap in micron -->
          <psk3dx:supportfill>0.2</psk3dx:supportfill><!-- sparse infill fraction for support (between 0 and 1, inclusive) -->
          <psk3dx:raftlayers>2</psk3dx:raftlayers><!-- number of solid raft layers -->
          <psk3dx:raftlayerthickness>600</psk3dx:raftlayerthickness><!-- layer thickness of the raft (micron) -->
          <psk3dx:raftpathwidth>2000</psk3dx:raftpathwidth><!-- path width of raft (micron) -->
          <psk3dx:raftfill>0.6</psk3dx:raftfill><!-- sparse infill fraction for support (between 0 and 1, inclusive) -->
          <psk3dx:raftoffset>2000</psk3dx:raftoffset><!-- size of the raft (micron) -->
          <psk3dx:raftzgap>500</psk3dx:raftzgap><!-- The Z gap (micron) -->
          <psk3dx:raftspeedfirst>20000</psk3dx:raftspeedfirst><!-- speed of raft first layer (micron/s) -->
          <psk3dx:coolingtime>5</psk3dx:coolingtime><!-- cooling time for a layer (second) -->
          <psk3dx:rampuptarget>500</psk3dx:rampuptarget> <!-- Z target for the fan to run at full speed -->
          <psk3dx:mincoolingspeed>1000</psk3dx:mincoolingspeed><!-- the minimum cooling speed for a layer (micron/s) -->
          <psk3dx:bridgingspeed>10000</psk3dx:bridgingspeed><!-- the speed for bridging (micron/s) -->
        </psk3dx:draft>
      </psk3dx:print>

  </psk3dx:MS3DPrinter>

</PrintDeviceCapabilities>
```



