---
title: Troubleshooting the metadata authoring wizards
description: Troubleshooting the metadata authoring wizards
ms.assetid: EBAF4289-DA23-4FFE-8CC0-DD21021CBA86
keywords:
- Troubleshooting the Metadata Authoring Wizard
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Troubleshooting the metadata authoring wizards


\[This topic describes the Device Metadata Authoring tool provided in the Windows Driver Kit (WDK) 8. If you’re developing device experiences for Windows 8.1, use the Device Metadata Authoring Wizard available with [Microsoft Visual Studio 2013 and Windows Driver Kit (WDK) 8.1](http://go.microsoft.com/fwlink/p/?LinkId=226411). For more information, see [Windows 8.1 device experience](http://go.microsoft.com/fwlink/p/?linkid=325561). \]

If you receive any of the following error messages, refer to the Resolution column in the table to resolve the issue.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Tool</td>
<td align="left">Screen</td>
<td align="left">Error message</td>
<td align="left">Resolution</td>
</tr>
<tr class="even">
<td align="left">Metadata Authoring Wizard</td>
<td align="left">Welcome</td>
<td align="left">ERROR: You must specify a folder location</td>
<td align="left">Enter a folder path.</td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left">Welcome</td>
<td align="left">ERROR: FolderLocation.Text folder does not exist</td>
<td align="left">Correct the file path.</td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left">Welcome</td>
<td align="left">The chosen file doesn&#39;t exist</td>
<td align="left">Correct the file path or name.</td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left">Welcome</td>
<td align="left">XML File error</td>
<td align="left"><p>Correct the XML error.</p>
<p>Error examples:</p>
<ul>
<li>Was expecting the first child of {0} to be {1}, but found {2} instead.</li>
<li>Was expecting {0} to be followed by {1}, but found {2} instead.</li>
</ul></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left">Finish</td>
<td align="left">Package creation failed:</td>
<td align="left"><p>Change the parameter based on the instructions.</p>
<p>Error examples:</p>
<ul>
<li>You must specify the ModelName for the device (locale {0})</li>
<li>You must associate this package with at least one HardwareID or ModelID</li>
<li>You must specify a primary category for this device</li>
</ul>
<p>Warning examples:</p>
<ul>
<li>ModelNumber ({0}) is not specified</li>
<li>DeviceDescription 2 ({0}) is not specified</li>
<li>The generic icon will be determined by the primary category selection</li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left">Association</td>
<td align="left">Invalid format : &quot;Value&quot; - don&#39;t add { } in the beginning and end.</td>
<td align="left">Remove the {} and try again.</td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left">Association</td>
<td align="left">Invalid GUID format: &quot;Value&quot;</td>
<td align="left">Type the correct GUID and try again.</td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left">Icon</td>
<td align="left">There were problems with the icon file: &quot;Error Message&quot; Icon Validation Error</td>
<td align="left">The icon can&#39;t be found or doesn&#39;t meet the requirement to be displayed in Devices and Printers in Control Panel. Find or fix the icon and try again.
<p>Error examples:</p>
<ul>
<li>Error: Image 256x256 transparency needs to be set.</li>
<li>Error: Image 48x48:32bit+Alpha does not exist.</li>
</ul></td>
</tr>
<tr class="even">
<td align="left">Submission Wizard</td>
<td align="left">Select metadata packages</td>
<td align="left">There is already a package with that name in the list</td>
<td align="left">Create a new GUID for the device metadata package.</td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left">Select metadata packages</td>
<td align="left">There was a problem loading the package:</td>
<td align="left">Change the parameter based on the instructions.</td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left">Finish</td>
<td align="left">There was a problem creating the submission package:</td>
<td align="left">Change the parameter based on the instructions.</td>
</tr>
</tbody>
</table>

 

 

 





