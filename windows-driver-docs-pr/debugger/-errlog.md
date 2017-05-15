---
title: errlog
description: The errlog extension displays the contents of any pending entries in the I/O system's error log.
ms.assetid: 2ef6331e-fa83-4515-8d70-5094e40b8497
keywords: ["errlog Windows Debugging"]
topic_type:
- apiref
api_name:
- errlog
api_type:
- NA
---

# !errlog


The **!errlog** extension displays the contents of any pending entries in the I/O system's error log.

``` syntax
    !errlog 
```

## <span id="ddk__errlog_dbg"></span><span id="DDK__ERRLOG_DBG"></span>


### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Kdextx86.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about [**IoWriteErrorLogEntry**](https://msdn.microsoft.com/library/windows/hardware/ff550527), see the Windows Driver Kit (WDK) documentation.

Remarks
-------

This command displays information about any pending events in the I/O system's error log. These are events queued by calls to the [**IoWriteErrorLogEntry**](https://msdn.microsoft.com/library/windows/hardware/ff550527) function, to be written to the system's event log for subsequent viewing by the **Event Viewer**.

Only entries that were queued by [**IoWriteErrorLogEntry**](https://msdn.microsoft.com/library/windows/hardware/ff550527) but have not been committed to the error log will be displayed.

This command can be used as a diagnostic aid after a system crash because it reveals pending error information that was unable to be committed to the error log before the system halted.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!errlog%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




