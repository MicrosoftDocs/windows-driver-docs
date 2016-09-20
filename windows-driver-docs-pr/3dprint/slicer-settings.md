---
title: Slicer settings
author: windows-driver-content
description: The configuration file contains a number of settings that may need to be adjusted for a specific 3D printer device.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9203AABB-48D9-47A6-A2B1-7A878BF82FD1
---

# Slicer settings


The configuration file contains a number of settings that may need to be adjusted for a specific 3D printer device.

## Slicer settings


<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Setting</th>
<th>Change</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>psk3d:Job3DOutputArea\ </p>
<p>psk3d:Job3DOutputAreaWidth</p>
<p>psk3d:Job3DOutputArea\ </p>
<p>psk3d:Job3DOutputAreaDepth</p>
<p>psk3d:Job3DOutputArea\ </p>
<p>psk3d:Job3DOutputAreaHeight</p></td>
<td><p>Yes</p></td>
<td><p>Print volume in microns, defined by width (x max), depth (y max), and height (z max).</p></td>
</tr>
<tr class="even">
<td><p>psk3d:Job3DMaterials\</p>
<p>psk3d:[Material]\</p>
<p>psk3dx:platformtemperature</p></td>
<td><p>Yes</p></td>
<td><p>The temperature (degrees Celsius) the print bed should be heated to during printing. A value of 0 means the bed should not be heated.</p>
<p>This value can be referenced via the <em>$platformtemperature$</em> template in the pre-commands.</p></td>
</tr>
<tr class="odd">
<td><p>psk3d:Job3DMaterials\</p>
<p>psk3d:[Material]\psk3dx:filamentdiameter</p></td>
<td><p>Yes</p></td>
<td><p>The diameter in microns of the filament loaded in the 3D printer. For example, 1750 is standard 1.75mm filament.</p></td>
</tr>
<tr class="even">
<td><p>psk3d:Job3DMaterials\</p>
<p>psk3d:[Material]\</p>
<p>psk3dx:filamentcalibrationoverride</p></td>
<td><p>Optional</p></td>
<td><p>A factor that adjusts the flow of filament. It is applied as a ratio of the incoming filament cross-section (based on filamentdiameter) to adjust the speed of extrusion. If this factor is greater than 1.0, less plastic will be extruded. This is a tuning parameter and should always be near 1.0.</p></td>
</tr>
<tr class="odd">
<td><p>psk3d:Job3DMaterials\</p>
<p>psk3d:[Material]\</p>
<p>psk3dx:extrudertemperature</p></td>
<td><p>Yes</p></td>
<td><p>The temperature in degrees Celsius the extruder/hot end should heat to when extruding. This value can be referenced via the <em>$extrudertemperature$</em> template in the pre-commands.</p></td>
</tr>
<tr class="even">
<td><p>psk3d:Job3DMaterials\</p>
<p>psk3d:[Material]\</p>
<p>psk3dx:autocenter</p></td>
<td><p>Optional</p></td>
<td><p>A Boolean value (0 or 1) indicating whether the model should be centered on the print bed (on the XY plane).</p></td>
</tr>
<tr class="odd">
<td><p>psk3dx:customStatus</p></td>
<td><p>Optional</p></td>
<td><p>A string representing the initial print job status, typically the slicing phase. If missing, the job status will be set to &quot;Printing&quot;.</p></td>
</tr>
<tr class="even">
<td><p>psk3dx:userprompt</p></td>
<td><p>Yes</p></td>
<td><p>A message displayed as the user prompt before a print begins. This prompt is used to prevent the extruder crashing into a previous print on devices that require manual removal of prints.</p>
<p>For devices that can display the prompt on device itself this setting is not required.</p></td>
</tr>
<tr class="odd">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:debug\</p>
<p>psk3dx:log</p></td>
<td><p>Optional</p></td>
<td><p>When present, this setting enables driver debug logging to a file.</p>
<p>This setting can also be turned on globally via registry key HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Print</p>
<p>StandardGCodeDebugLog=&quot;c:\Path\To\LogFile&quot;</p></td>
</tr>
<tr class="even">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:communication\</p>
<p>psk3dx:connection\</p>
<p>psk3dx:comport</p></td>
<td><p>Optional</p></td>
<td><p>URI to a serial port name. When present, this setting overrides the driver auto-resolution of the COM port (Printer Queue -&gt; Printer Port Name -&gt; Enum\3DPrinter\Device -&gt; Enum\USB\Serial Device).</p></td>
</tr>
<tr class="odd">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:communication\</p>
<p>psk3dx:connection\</p>
<p>psk3dx:baudrate</p></td>
<td><p>Optional</p></td>
<td><p>The baud rate of the serial connection for the connected device. Typical values are 115200 or 250000.</p></td>
</tr>
<tr class="even">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:communication\</p>
<p>psk3dx:connection\</p>
<p>psk3dx:mode</p></td>
<td><p>Reserved</p></td>
<td><p>This setting controls the reset on connect behavior (DTR setting). Use values of 1 or 3 if the device fails to connect.</p></td>
</tr>
<tr class="odd">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:communication\</p>
<p>psk3dx:connection\</p>
<p>psk3dx:timeout</p></td>
<td><p>Reserved</p></td>
<td><p>Timeout in milliseconds for printer response. Use a value of 0 (default) for no timeout.</p></td>
</tr>
<tr class="even">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:customcommands\</p>
<p>psk3dx:initcommands\</p>
<p>psk3dx:command</p></td>
<td><p>Yes</p></td>
<td><p>The sequence of commands sent before slicing. These commands are executed in parallel with the slicer. This is typically a sequence of G-Code commands that home, calibrate, auto-level and/or heat up the printer to a near final temperature.</p></td>
</tr>
<tr class="odd">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:customcommands\</p>
<p>psk3dx:precommands\</p>
<p>psk3dx:command</p></td>
<td><p>Yes</p></td>
<td><p>The set of G-Code commands to send at the start of each job, generally to initialize the 3D printer, like homing and heating up the extruder to the final temperature and priming the extruder. Each device has different required pre-commands. Each line of G-Code should appear in a child &lt;command&gt; element. Variables that are to be replaced by the referenced setting can be declared as the name delimited by ‘$’ characters, for example, &lt;command&gt;M104 <em>S$extrudertemperature$</em>&lt;/command&gt;.</p></td>
</tr>
<tr class="even">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:customcommands\</p>
<p>psk3dx:postcommands\</p>
<p>psk3dx:command</p></td>
<td><p>Yes</p></td>
<td><p>The set of G-Code commands to send at the end of each job, generally to bring the 3D printer to a safe state, like cooling down the extruder and moving the part away from the extruder/hot end to where it's easy to remove from the bed. Each device has different required post-commands.</p>
<p>This sequence is also executed when a job is cancelled.</p></td>
</tr>
<tr class="odd">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:customcommands\</p>
<p>psk3dx:failsafepostcommands\</p>
<p>psk3dx:command</p></td>
<td><p>Optional</p></td>
<td><p>A set of G-Code commands to be sent as fail safe mechanism, for example, in case of a slicer error. If missing, the driver will execute an &quot;M110 N0&quot; followed by &quot;M104 S0&quot;.</p></td>
</tr>
<tr class="even">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:layerthickness</p></td>
<td><p>Yes</p></td>
<td><p>The thickness (z-height) of a layer in microns. This value should be defined based on the machine physical resolution to minimize the positioning errors.</p></td>
</tr>
<tr class="odd">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:maxlayerthickness</p></td>
<td><p>Reserved</p></td>
<td><p>Maximum layer thickness in microns.</p>
<p>This setting is reserved and may be deprecated in the future.</p></td>
</tr>
<tr class="even">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:minlayerthickness</p></td>
<td><p>Reserved</p></td>
<td><p>Minimum layer thickness in microns.</p>
<p>This setting is reserved and may be deprecated in the future.</p></td>
</tr>
<tr class="odd">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:pathwidth</p></td>
<td><p>Yes</p></td>
<td><p>The width (in the XY plane) of an extruded toolpath in microns. A value close to and slightly larger than the nozzle diameter tends to produce best results.</p></td>
</tr>
<tr class="even">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:shells</p></td>
<td><p>Optional</p></td>
<td><p>An integer number of inset shells before infill begins. A value of 1 makes only a single perimeter and a value of 0 makes only infill (very rough surface finish).</p></td>
</tr>
<tr class="odd">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:shelloffset</p></td>
<td><p>Optional</p></td>
<td><p>Offset of the outer shells in microns. Use this value to tune the results on models that have a very tight fit between parts (for example, gears).</p></td>
</tr>
<tr class="even">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:topsurfacelayers</p></td>
<td><p>Optional</p></td>
<td><p>An integer number of layers to fill solidly on the upper surfaces of the print. A value of 0 makes sparse infill visible from the top.</p></td>
</tr>
<tr class="odd">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:bottomsurfacelayers</p></td>
<td><p>Optional</p></td>
<td><p>An integer number of layers to fill solidly on the lower surfaces of the print. A value of 0 makes sparse infill visible from the bottom.</p></td>
</tr>
<tr class="even">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:fill</p></td>
<td><p>Reserved</p></td>
<td><p>Specifies the sparse infill fraction, between 0.0 and 1.0 inclusive. 0.1 (10%) is a good default. A value of 0.0 will result in only the shells being printed and a value of 1.0 will use the solid infill pattern instead of a sparse infill.</p>
<p>This setting is reserved and may be deprecated in the future.</p></td>
</tr>
<tr class="odd">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:fillangle</p></td>
<td><p>Optional</p></td>
<td><p>The initial angle of the fill pattern, measured in degrees along the XY (horizontal) plane, counter-clockwise from the X-axis.</p></td>
</tr>
<tr class="even">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:filloverlap</p></td>
<td><p>Reserved</p></td>
<td><p>Infill overlap (between 0 and 1 of the path width, inclusive).</p>
<p>This setting is reserved and may be deprecated in the future.</p></td>
</tr>
<tr class="odd">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:speed</p></td>
<td><p>Yes</p></td>
<td><p>The default speed for printing movements, in microns/second. This is the 2-norm of the X and Y axis speeds.</p></td>
</tr>
<tr class="even">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:speedouter</p></td>
<td><p>Yes</p></td>
<td><p>Speed of the outer perimeter (first shell) in microns/second. This can be set lower than the normal speed to create a better surface finish on the print.</p></td>
</tr>
<tr class="odd">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:speedfirst</p></td>
<td><p>Yes</p></td>
<td><p>Speed of the first layer (superseding <strong>speedouter</strong>) in microns/second. This can be set lower than the normal speed to create better print bed adhesion.</p></td>
</tr>
<tr class="even">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:speedtravel</p></td>
<td><p>Yes</p></td>
<td><p>Speed of non-extrusion moves in microns/second. This can be set higher than the normal speed to minimize stringing and speed up the print when the extruder is the limiting factor.</p></td>
</tr>
<tr class="odd">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:speedretract</p></td>
<td><p>Yes</p></td>
<td><p>Speed of filament retraction and push-back in microns/second. Unlike other speed settings, this is measured on the input filament, rather than on the X and Y axes. This speed is therefore about a factor of 20 smaller than the speeds above (depending on your filament). However, it can be higher than the equivalent speed, because plastic is not being forced to extrude during retraction.</p></td>
</tr>
<tr class="even">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:retraction</p></td>
<td><p>Yes</p></td>
<td><p>Length of filament to be retracted, again measured on input filament, in microns. This is symmetric for retracting and pushing back and is designed to reduce stringing and oozing of the nozzle when traveling.</p></td>
</tr>
<tr class="odd">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:supportorientationoptimization</p></td>
<td><p>Reserved</p></td>
<td><p>A Boolean value (0 or 1) indicating whether to automatically reorient the model to minimize required support, or not.</p>
<p>This setting is reserved and may be deprecated in the future.</p></td>
</tr>
<tr class="even">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:supportoverhangangle</p></td>
<td><p>Optional</p></td>
<td><p>The maximum overhang angle requiring support, measured from the horizontal plane up to the model facet, in degrees. Smaller angles create less support structure.</p></td>
</tr>
<tr class="odd">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:supportzgap</p></td>
<td><p>Yes</p></td>
<td><p>The Z gap in microns between the part and support. This setting can reduce the adhesion to support, making the support easier to remove.</p></td>
</tr>
<tr class="even">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:supportxygap</p></td>
<td><p>Yes</p></td>
<td><p>The gap in micron between support and part in the XY plane.</p></td>
</tr>
<tr class="odd">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:supportfill</p></td>
<td><p>Optional</p></td>
<td><p>Sparse infill fraction for support (between 0 and 1, inclusive).</p></td>
</tr>
<tr class="even">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:raftlayers</p></td>
<td><p>Optional</p></td>
<td><p>Number of solid raft layers. A number of 2 is generally sufficient.</p></td>
</tr>
<tr class="odd">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:raftlayerthickness</p></td>
<td><p>Yes</p></td>
<td><p>Layer thickness (Z height) of the raft in microns.</p></td>
</tr>
<tr class="even">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:raftpathwidth</p></td>
<td><p>Yes</p></td>
<td><p>Path width of raft in microns. This is generally a larger value to accommodate variations in the print bed surface.</p></td>
</tr>
<tr class="odd">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:raftfill</p></td>
<td><p>Optional</p></td>
<td><p>Sparse infill fraction for support (between 0 and 1, inclusive).</p></td>
</tr>
<tr class="even">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:raftoffset</p></td>
<td><p>Optional</p></td>
<td><p>Size of the raft in microns.</p></td>
</tr>
<tr class="odd">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:raftzgap</p></td>
<td><p>Yes</p></td>
<td><p>The Z gap in microns between the raft and the object. A higher value makes the raft easier to remove, but might produce an uneven surface.</p></td>
</tr>
<tr class="even">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:raftspeedfirst</p></td>
<td><p>Yes</p></td>
<td><p>Speed of raft first layer in microns/second. This should be similar or lower to <strong>speedfirst</strong> to increase bed adhesion.</p></td>
</tr>
<tr class="odd">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:coolingtime</p></td>
<td><p>Optional</p></td>
<td><p>Minimum cooling time for a layer in seconds. The layer speed is reduced such that at it prints in more than this number of seconds.</p></td>
</tr>
<tr class="even">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:mincoolingspeed</p></td>
<td><p>Optional</p></td>
<td><p>The minimum cooling speed for a layer in microns/second.</p></td>
</tr>
<tr class="odd">
<td><p>psk3dx:MS3DPrinter\</p>
<p>psk3dx:print\</p>
<p>psk3dx:{quality}\</p>
<p>psk3dx:bridgingspeed</p></td>
<td><p>Yes</p></td>
<td><p>The speed of extrusion during bridging in microns. This value depends on factors such as machine cooling characteristics and filament type and is typically slower than normal printing speed.</p></td>
</tr>
</tbody>
</table>

 

**Note**   In the print node's settings (psk3dx:MS3DPrinter\\psk3dx:print\\psk3dx:{quality}\), the {quality} element name is replaced by one of the corresponding psk3d:Quality Print Schema 3D Keyword settings sent in the PrintTicket along with the print job. This allows each quality level to define its own set of slicer settings. If the PrintTicket is omitted, the slicer will use the \[quality\] setting marked with the attribute default="true", so exactly one quality level should always define this attribute.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


