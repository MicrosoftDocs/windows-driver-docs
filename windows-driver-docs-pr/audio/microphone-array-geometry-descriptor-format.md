---
title: Microphone Array Geometry Descriptor Format
description: Microphone Array Geometry Descriptor Format
ms.assetid: 83fae1e2-cc67-4322-8250-f642508383ef
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Microphone Array Geometry Descriptor Format


A USB audio microphone array must describe itself to the system to which it is connected. This means that the parameters that are required to describe the array must be embedded in the array device itself. Array geometry information is retrieved from the device by using a [GET\_MEM](https://go.microsoft.com/fwlink/p/?linkid=143724) request.

Information about USB audio device geometry must be provided in a standard format. As such, USB microphone arrays that are intended to work with the Windows Vista USB audio class driver must provide a descriptor that uses the information format that is defined in the following table.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Offset</th>
<th align="left">Field</th>
<th align="left">Size</th>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>guidMicArrayID</p></td>
<td align="left"><p>16</p></td>
<td align="left"><p>Globally unique identifier (GUID)</p></td>
<td align="left"><p>A unique ID that marks the beginning of the microphone array information in memory ( {07FE86C1-8948-4db5-B184-C5162D4AD314} ).</p></td>
</tr>
<tr class="even">
<td align="left"><p>16</p></td>
<td align="left"><p>wDescriptorLength</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Number</p></td>
<td align="left"><p>The length in bytes of the microphone array information, including the GUID and length fields.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>18</p></td>
<td align="left"><p>wVersion</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Binary coded decimal (BCD)</p></td>
<td align="left"><p>The version number of the microphone array specification, followed by this descriptor.</p></td>
</tr>
<tr class="even">
<td align="left"><p>20</p></td>
<td align="left"><p>wMicArrayType</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Number</p></td>
<td align="left"><p>The following values are defined:</p>
<p>00: Linear.</p>
<p>01: Planar.</p>
<p>02: 3-dimensional (3D).</p>
<p>03-FFFF: Reserved</p></td>
</tr>
<tr class="odd">
<td align="left"><p>22</p></td>
<td align="left"><p>wWorkVertAngBeg</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Number</p></td>
<td align="left"><p>The start of the work volume vertical angle.</p></td>
</tr>
<tr class="even">
<td align="left"><p>24</p></td>
<td align="left"><p>wWorkVertAngEnd</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Number</p></td>
<td align="left"><p>The end of the work volume vertical angle.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>26</p></td>
<td align="left"><p>wWorkHorAngBeg</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Number</p></td>
<td align="left"><p>The beginning of the work volume horizontal angle.</p></td>
</tr>
<tr class="even">
<td align="left"><p>28</p></td>
<td align="left"><p>wWorkHorAngEnd</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Number</p></td>
<td align="left"><p>The end of the work volume horizontal angle.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>30</p></td>
<td align="left"><p>wWorkFreqBandLo</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Number</p></td>
<td align="left"><p>The lower bound of the work frequency range.</p></td>
</tr>
<tr class="even">
<td align="left"><p>32</p></td>
<td align="left"><p>wWorkFreqBandHi</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Number</p></td>
<td align="left"><p>The upper bound of the work frequency range.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>34</p></td>
<td align="left"><p>wNumberOfMics</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Number</p></td>
<td align="left"><p>The number of individual microphone definitions that follow.</p></td>
</tr>
<tr class="even">
<td align="left"><p>36</p></td>
<td align="left"><p>wMicrophoneType(0)</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Number</p></td>
<td align="left"><p>A number that uniquely identifies the type of microphone 0:</p>
<p>00: Omni-Directional</p>
<p>01: SubCardioid</p>
<p>02: Cardioid</p>
<p>03: SuperCardioid</p>
<p>04: HyperCardioid</p>
<p>05: 8 Shaped</p>
<p>0F - FF: Vendor defined</p></td>
</tr>
<tr class="odd">
<td align="left"><p>38</p></td>
<td align="left"><p>wXCoordinate(0)</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Number</p></td>
<td align="left"><p>The x-coordinate of microphone 0.</p></td>
</tr>
<tr class="even">
<td align="left"><p>40</p></td>
<td align="left"><p>wYCoordinate(0)</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Number</p></td>
<td align="left"><p>The y-coordinate of microphone 0.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>42</p></td>
<td align="left"><p>wZCoordinate(0)</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Number</p></td>
<td align="left"><p>The z-coordinate of microphone 0.</p></td>
</tr>
<tr class="even">
<td align="left"><p>44</p></td>
<td align="left"><p>wMicVertAngle(0)</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Number</p></td>
<td align="left"><p>The main response axis (MRA) vertical angle of microphone 0.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>46</p></td>
<td align="left"><p>wMicHorAngle(0)</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Number</p></td>
<td align="left"><p>The MRA horizontal angle of microphone 0.</p></td>
</tr>
<tr class="even">
<td align="left"><p>...</p></td>
<td align="left"><p>...</p></td>
<td align="left"><p>...</p></td>
<td align="left"><p>...</p></td>
<td align="left"><p>Microphone definitions 1 to n-2.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>34+((n-1)<em>12)</p></td>
<td align="left"><p>wMicType(n-1)</p></td>
<td align="left"></td>
<td align="left"><p>Number</p></td>
<td align="left"><p>A number that uniquely identifies the type of microphone n-1:</p>
<p>00: Omni-Directional</p>
<p>01: SubCardioid</p>
<p>02: Cardioid</p>
<p>03: SuperCardioid</p>
<p>04: HyperCardioid</p>
<p>05: 8 Shaped</p>
<p>0F - FF: Vendor defined</p></td>
</tr>
<tr class="even">
<td align="left"><p>36+((n-1)</em>12)</p></td>
<td align="left"><p>wXCoordinate(n-1)</p></td>
<td align="left"></td>
<td align="left"><p>Number</p></td>
<td align="left"><p>The x-coordinate of microphone n-1.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>38+((n-1)<em>12)</p></td>
<td align="left"><p>wYCoordinate(n-1)</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Number</p></td>
<td align="left"><p>The y-coordinate of microphone n-1.</p></td>
</tr>
<tr class="even">
<td align="left"><p>40+((n-1)</em>12)</p></td>
<td align="left"><p>wZCoordinate(n-1)</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Number</p></td>
<td align="left"><p>The z-coordinate of microphone n-1.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>42+((n-1)<em>12)</p></td>
<td align="left"><p>wMicVertAngle(n-1)</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Number</p></td>
<td align="left"><p>The MRA vertical angle of microphone n-1.</p></td>
</tr>
<tr class="even">
<td align="left"><p>44+((n-1)</em>12)</p></td>
<td align="left"><p>wMicHorAngle(n-1)</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Number</p></td>
<td align="left"><p>The MRA horizontal angle of microphone n-1.</p></td>
</tr>
</tbody>
</table>

 

For a detailed example about how to use this information format in a descriptor for a 4-element microphone array, see Appendix A of the [How to Build and Use Microphone Arrays for Windows Vista](https://go.microsoft.com/fwlink/p/?linkid=306613) white paper.

**Note**  

 

-   When you include a version number in the microphone array information, it allows the descriptor to be updated after the original specifications are implemented. The version number is a BCD value. For example, the current version (1.0) is represented as 0x0100.

-   The offset and size values are in bytes.

-   All angles are expressed in units of 1/10000 radians. For example, 3.1416 radians is expressed as 31416. The value can range from -31416 to 31416, inclusive.

-   X-y-z coordinates are expressed in millimeters. The value can range from -32767 to 32767, inclusive.

-   For information about the orientation, axes, and the positive directions of the angles of the coordinate system, see Appendix B in the microphone array white paper.

-   Frequency values are expressed in Hz. The range of frequency values is bounded only by the size of the field from **wWorkFreqBandLo** to **wWorkFreqBandHi**.

 

 




