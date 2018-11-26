---
title: Slicer settings
description: The configuration file XML contains a number of settings that need to be adjusted for a specific 3D Printer device to control the print capabilities exposed to the 3D Print Dialog in Windows.
ms.assetid: 9203AABB-48D9-47A6-A2B1-7A878BF82FD1
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Slicer settings


The configuration file XML contains a number of settings that need to be adjusted for a specific 3D Printer device to control the print capabilities exposed to the 3D Print Dialog in Windows. These settings also control Microsoft 3D Slicer (MS3DPrinterRenderFilter.DLL and dependencies) running parameters.  

## Slicer settings


<table>

<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>

<thead>
<tr class="header">
<th>Setting (XML Path)</th>
<th>Change</th>
<th>Description</th>
</tr>
</thead>

<tbody>

<tr>
<td><p>psk3d:Job3DOutputArea\ </p>
<p>psk3d:Job3DOutputAreaWidth</p>
<p>psk3d:Job3DOutputArea\ </p>
<p>psk3d:Job3DOutputAreaDepth</p>
<p>psk3d:Job3DOutputArea\ </p>
<p>psk3d:Job3DOutputAreaHeight</p></td>
<td><p>Yes</p></td>
<td><p>Print volume in microns, defined by width (x max), depth (y max), and height (z max).</p>
<p>The volume should represent the capabilities of the physical device, as one of the tests in the certification phase when publishing the driver ensures the printer can use the declared volume.</p></td>
</tr>


<tr>
<td><p>psk3d:Job3DOutputArea\ </p>
<p>psk3d:Job3DOutputAreaOffsetX</p>
<p>psk3d:Job3DOutputArea\ </p>
<p>psk3d:Job3DOutputAreaOffsetX</p></td>
<td><p>Optional</p></td>
<td><p>X and Y offset of the print volume relative to (0, 0). This allows support for 3D printers where (0, 0) is in the center of the bed (typical for Delta printers) or printers where (0, 0) is not in the front left corner of the print bed.</p></td>
</tr>

<tr>
<td><p>psk3d:Job3DMaterials\ </p>
<p>psk3ds:extruders\  </p></td>
<td><p>Optional</p></td>
<td><p>The number of extruders in the printer. This setting controls how many of the subsequent psk3d:Material&lt;Mat&gt; sections in the XML will be sent to the print dialog as Print Capabilities. If not specified, the drivers will assume a single extruder printer.</p></td>
</tr>

<tr>
<td><p>psk3d:Job3DMaterials\ </p>
<p>psk3d:Material&lt;Material&gt;\ </p>
<p>psk:DisplayName</p></td>
<td><p>Yes</p></td>
<td><p>The display name of the material. This can be any string that shows up in the 3D Print Dialog for user assignment.</p></td>
</tr>

<tr>
<td><p>psk3d:Job3DMaterials\ </p>
<p>psk3d:Material&lt;Material&gt;\ </p>
<p>psk:MaterialColor</p></td>
<td><p>Yes</p></td>
<td><p>RGB or RGBA color for the material rendering in the 3D Print Dialog.</p></td>
</tr>

<tr>
<td><p>psk3d:Job3DMaterials\ </p>
<p>psk3d:Material&lt;Material&gt;\ </p>
<p>psk:MaterialType</p></td>
<td><p>Reserved</p></td>
<td><p>Type of material, as defined in Print Schema Keywords for 3D Printing (for example, &quot;psk3d:PLA&quot;). This setting is being deprecated in favor of generic materials specified by name and color.</p></td>
</tr>

<tr>
<td><p>psk3d:Job3DMaterials\ </p>
<p>psk3d:Material&lt;Material&gt;\ </p>
<p>psk3dx:platformtemperature</p></td>
<td><p>Yes</p></td>
<td><p>The temperature (degrees Celsius) the print bed should be heated to during printing. A value of 0 means the bed should not be heated.</p>
<p>This value can be later referenced via the <em>$platformtemperature$</em> template in the pre-commands.</p></td>
</tr>

<tr>
<td><p>psk3d:Job3DMaterials\ </p>
<p>psk3d:Material&lt;Material&gt;\ </p>
<p>psk3dx:filamentdiameter</p></td>
<td><p>Yes</p></td>
<td><p>The diameter in microns of the filament loaded in the 3D printer. For example, 1750 is standard 1.75mm filament.</p></td>
</tr>

<tr>
<td><p>psk3d:Job3DMaterials\ </p>
<p>psk3d:Material&lt;Material&gt;\ </p>
<p>psk3dx:filamentcalibrationoverride</p></td>
<td><p>Optional</p></td>
<td><p>A factor that adjusts the flow of filament. It is applied as a ratio of the incoming filament cross-section (based on filamentdiameter) to adjust the speed of extrusion. If this factor is greater than 1.0, less plastic will be extruded. This is a tuning parameter and should always be near 1.0.</p></td>
</tr>

<tr>
<td><p>psk3d:Job3DMaterials\ </p>
<p>psk3d:Material&lt;Material&gt;\ </p>
<p>psk3dx:extrudertemperature</p></td>
<td><p>Yes</p></td>
<td><p>The temperature in degrees Celsius the extruder/hot end should heat to when extruding. This value can be referenced via the <em>$extrudertemperature$</em> template in the pre-commands.</p></td>
</tr>

<tr>
<td><p>psk3d:Job3DMaterials\ </p>
<p>psk3d:Material&lt;Material&gt;\ </p>
<p>psk3dx:autocenter</p></td>
<td><p>Optional</p></td>
<td><p>A Boolean value (0 or 1) indicating whether the model should be centered on the print bed (on the XY plane). The model is also auto-centered if it does not fit in the print volume.</p></td>
</tr>

<tr>
<td><p>psk3d:Job3DMaterials\  </p>
<p>psk3d:Material&lt;Material&gt;\  </p>
<p>psk3dx:SetupCommands\ </p>
<p>psk3dx:command</p></td>
<td><p>Yes</p></td>
<td><p>A list of commands to use as material set-up. This is typically G-Code executed during pre-commands to control nozzle pre-heating, priming, and so on.</p></td>
</tr>

<tr>
<td><p>psk3d:Job3DMaterials\  </p>
<p>psk3d:Material&lt;Material&gt;\  </p>
<p>psk3dx:SelectCommands\ </p>
<p>psk3dx:command</p></td>
<td><p>Yes</p></td>
<td><p>A list of commands to issue when the material needs to be used while printing. This is typically G-Code executed for: T0/T1 extruder selection, nozzle wiping sequence, turn fan on/off/gradual, retract the material, temperature, and so on.</p></td>
</tr>

<tr>
<td><p>psk3d:Job3DMaterials\  </p>
<p>psk3d:Material&lt;Material&gt;\  </p>
<p>psk3dx:DeselectCommands\ </p>
<p>psk3dx:command</p></td>
<td><p>Yes</p></td>
<td><p>A list of commands to issue when the material is being released during printing. This is typically G-Code executed for: retract the material, park the nozzle, reduce temperature, and so on.</p></td>
</tr>

<tr>
<td><p>psk3dx:customStatus</p></td>
<td><p>Optional</p></td>
<td><p>A string representing the initial print job status, typically the slicing phase. If missing, the job status will be set to &quot;Printing&quot;. Typically this value should be set to &quot;Slicing&quot; when the slicing happens in the render filter, for example, when using the Microsoft Slicer.</p></td>
</tr>

<tr>
<td><p>psk3dx:userprompt</p></td>
<td><p>Yes</p></td>
<td><p>A message displayed as the user prompt before a print begins. This prompt is used to prevent the extruder from crashing into an existing print on devices that require manual removal of prints.</p>
<p>For devices that can display the prompt on the device itself at the beginning or end of print, this setting is not required.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:debug\ </p>
<p>psk3dx:log</p></td>
<td><p>Optional</p></td>
<td><p>When present, this setting enables driver debug logging to a file, allowing a developer to inspect the G-Code and firmware responses.</p>
<p>This setting can also be turned on globally via registry key HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Print</p>
<p>StandardGCodeDebugLog=&quot;c:\Path\To\LogFile&quot;</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:communication\ </p>
<p>psk3dx:connection\ </p>
<p>psk3dx:comport</p></td>
<td><p>Optional</p></td>
<td><p>URI to a serial port name. When present, this setting overrides the driver auto-resolution of the COM port (Printer Queue -&gt; Printer Port Name -&gt; Enum\3DPrinter\Device -&gt; Enum\USB\Serial Device). This allows temporarily printing to a device that does not have final hardware IDs.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:communication\ </p>
<p>psk3dx:connection\ </p>
<p>psk3dx:baudrate</p></td>
<td><p>Optional</p></td>
<td><p>The baud rate of the serial connection for the connected device. Typical values are 115200 or 250000.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:communication\ </p>
<p>psk3dx:connection\ </p>
<p>psk3dx:mode</p></td>
<td><p>Reserved</p></td>
<td><p>This setting controls the reset on connect behavior (DTR setting). Use values of 1 or 3 if the device fails to connect.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:communication\  </p>
<p>psk3dx:connection\ </p>
<p>psk3dx:protocol</p></td>
<td><p>Reserved</p></td>
<td><p>This setting is highly experimental and controls the communication protocol with the firmware. When not specified, the driver defaults to ASCII G-Code with RepRap/Marlin checksums. When set to 2, the driver can send binary G-Code.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:communication\ </p>
<p>psk3dx:connection\ </p>
<p>psk3dx:timeout</p></td>
<td><p>Reserved</p></td>
<td><p>Timeout in milliseconds for printer response. Use a value of 0 (default) for no timeout.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:customcommands\ </p>
<p>psk3dx:initcommands\ </p>
<p>psk3dx:command</p></td>
<td><p>Yes</p></td>
<td><p>The sequence of commands sent before slicing. These commands are executed in parallel with the slicer. This is typically a sequence of G-Code commands that home, calibrate, auto-level and/or heat up the printer to a near final temperature.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:customcommands\ </p>
<p>psk3dx:precommands\ </p>
<p>psk3dx:command</p></td>
<td><p>Yes</p></td>
<td><p>The set of G-Code commands to send at the start of each job, generally to initialize the 3D printer, like homing and heating up the extruder to the final temperature and priming the extruder. Each device has different required pre-commands. Each line of G-Code should appear in a child &lt;command&gt; element. Variables that are to be replaced by the referenced setting can be declared as the name delimited by ‘$’ characters, for example, &lt;command&gt;M104 <em>S$extrudertemperature$</em>&lt;/command&gt;. Refer to the next section for the built-in variables.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:customcommands\ </p>
<p>psk3dx:postcommands\ </p>
<p>psk3dx:command</p></td>
<td><p>Yes</p></td>
<td><p>The set of G-Code commands to send at the end of each job, generally to bring the 3D printer to a safe state, like cooling down the extruder and moving the part away from the extruder/hot end to where it&#39;s easy to remove from the bed. Each device has different required post-commands.</p>
<p>This sequence is also executed when a job is cancelled.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:customcommands\ </p>
<p>psk3dx:failsafepostcommands\ </p>
<p>psk3dx:command</p></td>
<td><p>Optional</p></td>
<td><p>A set of G-Code commands to be sent as fail safe mechanism, for example, in case of a slicer error. If missing, the driver will execute an &quot;M110 N0&quot; followed by &quot;M104 S0&quot;.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:layerthickness</p></td>
<td><p>Yes</p></td>
<td><p>The thickness (z-height) of a layer in microns. This value should be defined based on the machine physical resolution to minimize the positioning errors.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:maxlayerthickness</p></td>
<td><p>Reserved</p></td>
<td><p>Maximum layer thickness in microns.</p>
<p>This setting is reserved and may be deprecated in the future.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:minlayerthickness</p></td>
<td><p>Reserved</p></td>
<td><p>Minimum layer thickness in microns.</p>
<p>This setting is reserved and may be deprecated in the future.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:pathwidth</p></td>
<td><p>Yes</p></td>
<td><p>The width (in the XY plane) of an extruded toolpath in microns. A value close to and slightly larger than the nozzle diameter tends to produce best results.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:shells</p></td>
<td><p>Optional</p></td>
<td><p>An integer number of inset shells before infill begins. A value of 1 makes only a single perimeter and a value of 0 makes only infill (very rough surface finish).</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:shelloffset</p></td>
<td><p>Optional</p></td>
<td><p>Offset of the outer shells in microns. Use this value to tune the results on models that have a very tight fit between parts (for example, gears).</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:topsurfacelayers</p></td>
<td><p>Optional</p></td>
<td><p>An integer number of layers to fill solidly on the upper surfaces of the print. A value of 0 makes sparse infill visible from the top.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:bottomsurfacelayers</p></td>
<td><p>Optional</p></td>
<td><p>An integer number of layers to fill solidly on the lower surfaces of the print. A value of 0 makes sparse infill visible from the bottom.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:fill</p></td>
<td><p>Reserved</p></td>
<td><p>Specifies the sparse infill fraction, between 0.0 and 1.0 inclusive. 0.1 (10%) is a good default. A value of 0.0 will result in only the shells being printed and a value of 1.0 will use the solid infill pattern instead of a sparse infill.</p>
<p>This setting is reserved and may be deprecated in the future.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:fillangle</p></td>
<td><p>Optional</p></td>
<td><p>The initial angle of the fill pattern, measured in degrees along the XY (horizontal) plane, counter-clockwise from the X-axis.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:filloverlap</p></td>
<td><p>Reserved</p></td>
<td><p>Infill overlap (between 0 and 1 of the path width, inclusive).</p>
<p>This setting is reserved and may be deprecated in the future.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:speed</p></td>
<td><p>Yes</p></td>
<td><p>The default speed for printing movements, in microns/second. This is the 2-norm of the X and Y axis speeds.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:speedouter</p></td>
<td><p>Yes</p></td>
<td><p>Speed of the outer perimeter (first shell) in microns/second. This can be set lower than the normal speed to create a better surface finish on the print.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:speedfirst</p></td>
<td><p>Yes</p></td>
<td><p>Speed of the first layer (superseding <strong>speedouter</strong>) in microns/second. This can be set lower than the normal speed to create better print bed adhesion.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:speedtravel</p></td>
<td><p>Yes</p></td>
<td><p>Speed of non-extrusion moves in microns/second. This can be set higher than the normal speed to minimize stringing and speed up the print when the extruder is the limiting factor.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:speedretract</p></td>
<td><p>Yes</p></td>
<td><p>Speed of filament retraction and push-back in microns/second. Unlike other speed settings, this is measured on the input filament, rather than on the X and Y axes. This speed is therefore about a factor of 20 smaller than the speeds above (depending on your filament). However, it can be higher than the equivalent speed, because plastic is not being forced to extrude during retraction.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:retraction</p></td>
<td><p>Yes</p></td>
<td><p>Length of filament to be retracted, again measured on input filament, in microns. This is symmetric for retracting and pushing back and is designed to reduce stringing and oozing of the nozzle when traveling.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:supportorientationoptimization</p></td>
<td><p>Reserved</p></td>
<td><p>A Boolean value (0 or 1) indicating whether to automatically reorient the model to minimize required support, or not.</p>
<p>This setting is reserved and may be deprecated in the future.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:supportoverhangangle</p></td>
<td><p>Optional</p></td>
<td><p>The maximum overhang angle requiring support, measured from the horizontal plane up to the model facet, in degrees. Smaller angles create less support structure.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:supportzgap</p></td>
<td><p>Yes</p></td>
<td><p>The Z gap in microns between the part and support. This setting can reduce the adhesion to support, making the support easier to remove.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:supportxygap</p></td>
<td><p>Yes</p></td>
<td><p>The gap in micron between support and part in the XY plane.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:supportfill</p></td>
<td><p>Optional</p></td>
<td><p>Sparse infill fraction for support (between 0 and 1, inclusive).</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:raftlayers</p></td>
<td><p>Optional</p></td>
<td><p>Number of solid raft layers. A number of 2 is generally sufficient.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:raftlayerthickness</p></td>
<td><p>Yes</p></td>
<td><p>Layer thickness (Z height) of the raft in microns.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:raftpathwidth</p></td>
<td><p>Yes</p></td>
<td><p>Path width of raft in microns. This is generally a larger value to accommodate variations in the print bed surface.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:raftfill</p></td>
<td><p>Optional</p></td>
<td><p>Sparse infill fraction for support (between 0 and 1, inclusive).</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:raftoffset</p></td>
<td><p>Optional</p></td>
<td><p>Size of the raft in microns.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:raftzgap</p></td>
<td><p>Yes</p></td>
<td><p>The Z gap in microns between the raft and the object. A higher value makes the raft easier to remove, but might produce an uneven surface.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:raftspeedfirst</p></td>
<td><p>Yes</p></td>
<td><p>Speed of raft first layer in microns/second. This should be similar or lower to <strong>speedfirst</strong> to increase bed adhesion.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:coolingtime</p></td>
<td><p>Optional</p></td>
<td><p>Minimum cooling time for a layer in seconds. The layer speed is reduced such that at it prints in more than this number of seconds.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:mincoolingspeed</p></td>
<td><p>Optional</p></td>
<td><p>The minimum cooling speed for a layer in microns/second.</p></td>
</tr>

<tr>
<td><p>psk3dx:MS3DPrinter\ </p>
<p>psk3dx:print\ </p>
<p>psk3dx:{quality}\ </p>
<p>psk3dx:bridgingspeed</p></td>
<td><p>Yes</p></td>
<td><p>The speed of extrusion during bridging in microns. This value depends on factors such as machine cooling characteristics and filament type and is typically slower than normal printing speed.</p></td>
</tr>

</tbody>
</table>


**Note** In the print node's settings (psk3dx:MS3DPrinter\\psk3dx:print\\psk3dx:{quality}\), the {quality} element name is replaced by one of the corresponding psk3d:Quality Print Schema 3D Keyword settings sent in the PrintTicket along with the print job. This allows each quality level to define its own set of slicer settings. If the PrintTicket is omitted, the slicer will use the \[quality\] setting marked with the attribute default="true", so exactly one quality level should always define this attribute.

<table>

<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>

<thead>
<tr class="header">
<th>Setting name</th>
<th>Description</th>
</tr>
</thead>
<tbody>

<tr>
<td><p>$extrudertemperature$</p>
<p>$extruder2temperature$</p></td>
<td><p>The temperature of the first and respectively the second extruder, as specified by &lt;psk3dx:extrudertemperature&gt; in the Materials section in the XML. These variables are being deprecated and being replaced by $MaterialSetup$.</p></td>
</tr>

<tr>
<td><p>$platformtemperature$</p></td>
<td><p>The temperature of the heated bed as specified by the &lt;psk3dx:platformtemperature&gt; entry in the last material in the list.</p></td>
</tr>

<tr>
<td><p>$MaterialSetup<n>$</p></td>
<td><p>The material setup section &lt;psk3dx:SetupCommands&gt; in materials. For example $MaterialSetup3$ represents the 3rd material in the list, typically the 3rd extruder.</p></td>
</tr>

<tr>
<td><p>$rampup$</p></td>
<td><p>This is a variable that can be 0..255 and scales with Z axis and is controlled by the &lt;psk3dx:rampuptarget&gt; in the slicer quality settings.</p>
<p>For example a command &quot;M106 S$rampup$&quot; turns on the fan gradually as the Z axis increases. If the &lt;psk3dx:rampuptarget&gt; is set to 500 microns, the value of the variable would be  0 on the first layer, and 255 once the layer is at 500 microns or above.</p>
<p>This variable is intended to support for better print adhesion on heated print beds but it can be used in any command.</p></td>
</tr>

<tr>
<td><p>;?ack=&lt;pattern&gt;</p></td>
<td><p>This setting instructs the driver to change the command ACK pattern (the printer response) from the default &#39;ok&#39; to something temporary, for example &quot;;?ack=Writing to file&quot; would tell the driver to wait for a confirmation the printer is ready to write to the internal storage.</p></td>
</tr>

<tr>
<td><p>;?err=&lt;pattern&gt;</p></td>
<td><p>This setting instructs the driver to look for an additional error pattern in the printer response, in addition to the default &#39;error&#39;. For example “;?err=open failed” would tell the driver to fail if such a response is received (in this example the hardware would return this response if the internal SD card storage was not initialized or full).</p></td>
</tr>

<tr>
<td><p>;?wait=&lt;pattern&gt;</p></td>
<td><p>This setting instructs the driver to ignore the pattern, this is typically used for keep alive signals, and the default value is ‘;?wait=wait’.</p></td>
</tr>

</tbody>
</table>




