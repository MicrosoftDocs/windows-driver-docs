---
title: Service icon requirements
description: Service icon requirements
ms.assetid: ce018a26-f5ce-4fbb-8339-b3207ca5ed68
ms.topic: article
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Service icon requirements


A service icon is used to display the logo of the mobile network operator (MNO) or mobile virtual network operator (MVNO) in Windows Connection Manager.

The file must be an .ICO file with one of the following requirements:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>256x256:32bit+Alpha(compressed)</p></td>
<td><p>24x24:32bit+Alpha</p></td>
</tr>
<tr class="even">
<td><p>48x48:32bit+Alpha</p></td>
<td><p>24x24:8bit256</p></td>
</tr>
<tr class="odd">
<td><p>48x48:8bit256</p></td>
<td><p>24x24:4bit16</p></td>
</tr>
<tr class="even">
<td><p>48x48:4bit16</p></td>
<td><p>16x16:32bit+Alpha</p></td>
</tr>
<tr class="odd">
<td><p>32x32:32bit+Alpha</p></td>
<td><p>16x16:8bit256</p></td>
</tr>
<tr class="even">
<td><p>32x32:8bit256</p></td>
<td><p>16x16:4bit16</p></td>
</tr>
<tr class="odd">
<td><p>32x32:4bit16</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

 

The service icon is associated with the [ServiceIconFile](https://msdn.microsoft.com/library/windows/hardware/dn973162) element in the [ServiceInfo XML schema](https://msdn.microsoft.com/library/windows/hardware/dn973167) of a service metadata package.

## <span id="related_topics"></span>Related topics

- [Create a mobile broadband experience](https://msdn.microsoft.com/library/windows/hardware/dn236414.aspx)

 

 






