---
ms.assetid: EB2264A4-BAE8-446B-B9A5-19893936DDCA
title: Target platform on driver reference pages
description: In the Requirements block at the bottom of Microsoft driver reference pages, you''ll see an entry called Target Platform.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Target platform on driver reference pages

In the Requirements block at the bottom of Microsoft driver reference pages, you'll see an entry called **Target Platform**. This line lists editions of Windows to which the page applies.

Here's an example of such an entry:

![target platform set to universal in requirements block](images/TargetPlatform.png)

The values specified in **Target Platform** map to the values you can use in Visual Studio, in the **Target Platform** property under **Configuration Properties-&gt;Driver Settings-&gt;General**.

Here are the values you might see for **Target Platform**, and what they mean:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Term</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="Universal"></span><span id="universal"></span><span id="UNIVERSAL"></span>Universal</p></td>
<td align="left"><p>A driver binary in a Universal Windows driver can call this device driver interface (DDI).</p>
<p>A Universal Windows driver runs on the following Universal Windows Platform (UWP)-based editions of Windows 10:</p>
<ul>
<li>Windows 10 for desktop editions (Home, Pro, and Enterprise)</li>
<li>Windows 10 in S-Mode</li>
<li>Windows 10 Mobile</li>
<li>Windows 10 IoT Core</li>
<li>Windows Server 2016</li>
</ul>
<p>For more info, see <a href="getting-started-with-universal-drivers.md" data-raw-source="[Getting Started with Universal Windows drivers](getting-started-with-universal-drivers.md)">Getting Started with Universal Windows drivers</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Desktop"></span><span id="desktop"></span><span id="DESKTOP"></span>Desktop</p></td>
<td align="left"><p>A driver binary for Windows 10 for desktop editions or Windows Server 2016 can call this DDI.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Mobile"></span><span id="mobile"></span><span id="MOBILE"></span>Mobile</p></td>
<td align="left"><p>A driver binary for Windows 10 Mobile can call this DDI.</p></td>
</tr>
</tbody>
</table>

 

 

 





