---
title: Bug Check 0xED UNMOUNTABLE_BOOT_VOLUME
description: The UNMOUNTABLE_BOOT_VOLUME bug check has a value of 0x000000ED. This indicates that the I/O subsystem attempted to mount the boot volume and it failed.
ms.assetid: 7c4ab301-f110-4fc8-9ff8-242e0d2155fd
keywords: ["Bug Check 0xED UNMOUNTABLE_BOOT_VOLUME", "UNMOUNTABLE_BOOT_VOLUME"]
ms.author: domars
ms.date: 06/26/2017
topic_type:
- apiref
api_name:
- UNMOUNTABLE_BOOT_VOLUME
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xED: UNMOUNTABLE\_BOOT\_VOLUME


The UNMOUNTABLE\_BOOT\_VOLUME bug check has a value of 0x000000ED. This indicates that the I/O subsystem attempted to mount the boot volume and it failed.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## UNMOUNTABLE\_BOOT\_VOLUME Parameters


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>The device object of the boot volume</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The status code from the file system that describes why it failed to mount the volume</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

Resolution
----------

If you are debugging this error, use the !analyze -v extension. This extension displays relevant data specific error to the error.

This bug check is typically related to the failure of the OS Boot storage device such as hard drive. To attempt to validate the file system and the recover the boot record the following troubleshooting steps may be helpful.  

1. In Windows 10, use Troubleshoot > Advanced Options > Startup Repair. You may need to create bootable recovery media and boot from a USB drive or DVD to run the Windows Recovery Environment.
2. From the command prompt in the Windows Recovery Environment use CHKDSK /r to attempt to repair the file system.  
3. Use the bootrec command to fix master and boot records.    

If these steps are not successful it is possible that the hard drive has failed. Some hard drive vendors provide diagnostic tools that may help confirm a hardware failure.




 

 

 




