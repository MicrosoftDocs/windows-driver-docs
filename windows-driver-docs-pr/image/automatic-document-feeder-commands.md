---
title: Automatic Document Feeder Commands
description: Automatic Document Feeder Commands
ms.assetid: dd6664d6-4853-4f97-85cc-39a7879d523e
---

# Automatic Document Feeder Commands


## <span id="ddk_automatic_document_feeder_commands_si"></span><span id="DDK_AUTOMATIC_DOCUMENT_FEEDER_COMMANDS_SI"></span>


The commands in this section are for microdrivers that support an automatic document feeder (ADF). To report that your microdriver supports an automatic document feeder, set the **ADF** member in the [**SCANINFO**](https://msdn.microsoft.com/library/windows/hardware/ff547361) structure to 1 (or 2 if the ADF has a duplexer) during the CMD\_INITIALIZE command. This will cause the WIA Flatbed driver to add the needed properties for ADF control and use the commands in this section.

<span id="CMD_LOAD_ADF"></span><span id="cmd_load_adf"></span>CMD\_LOAD\_ADF  
Called by the WIA Flatbed driver to load a page into the ADF. If this command does not apply to the device, return E\_NOTIMPL. This command is optional for a device that automatically feeds a page.

<span id="CMD_UNLOAD_ADF"></span><span id="cmd_unload_adf"></span>CMD\_UNLOAD\_ADF  
Called by the WIA Flatbed driver to unload a page from the ADF. If this command does not apply to the device, return E\_NOTIMPL. This command is optional for a device that automatically unfeeds a page.

<span id="CMD_GETADFAVAILABLE"></span><span id="cmd_getadfavailable"></span>CMD\_GETADFAVAILABLE  
Called by the WIA Flatbed driver to determine whether an ADF is available for use. If an ADF is available, return S\_OK. If this command does not apply to the device, return E\_NOTIMPL.

<span id="CMD_GETADFHASPAPER"></span><span id="cmd_getadfhaspaper"></span>CMD\_GETADFHASPAPER  
Called by the WIA Flatbed driver to get the paper status of the device's ADF. Set the **lVal** member of the passed [**VAL**](https://msdn.microsoft.com/library/windows/hardware/ff548627) structure to the appropriate status value. (See CMD\_ADFGETSTATUS for possible status values.)

<span id="CMD_GETADFOPEN"></span><span id="cmd_getadfopen"></span>CMD\_GETADFOPEN  
Same as CMD\_GETADFREADY. This command is not currently used by the WIA Flatbed Driver.

<span id="CMD_GETADFSTATUS"></span><span id="cmd_getadfstatus"></span>CMD\_GETADFSTATUS  
Called by the WIA Flatbed driver to get the status of the ADF attached to the device. Set the **lVal** member of the passed [**VAL**](https://msdn.microsoft.com/library/windows/hardware/ff548627) structure to the appropriate status value. Possible status values are as follows.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Status</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>MCRO_ERROR_GENERAL_ERROR</p></td>
<td><p>General error.</p></td>
</tr>
<tr class="even">
<td><p>MCRO_ERROR_OFFLINE</p></td>
<td><p>The ADF or device is offline.</p></td>
</tr>
<tr class="odd">
<td><p>MCRO_ERROR_PAPER_EMPTY</p></td>
<td><p>The ADF has no paper.</p></td>
</tr>
<tr class="even">
<td><p>MCRO_ERROR_PAPER_JAM</p></td>
<td><p>The ADF has a paper jam.</p></td>
</tr>
<tr class="odd">
<td><p>MCRO_ERROR_PAPER_PROBLEM</p></td>
<td><p>The ADF has a paper problem.</p></td>
</tr>
<tr class="even">
<td><p>MCRO_ERROR_USER_INTERVENTION</p></td>
<td><p>The user needs to interact with the device.</p></td>
</tr>
<tr class="odd">
<td><p>MCRO_STATUS_OK</p></td>
<td><p>There is no error to report.</p></td>
</tr>
</tbody>
</table>

 

<span id="CMD_GETADFUNLOADREADY"></span><span id="cmd_getadfunloadready"></span>CMD\_GETADFUNLOADREADY  
Called by the WIA Flatbed Driver to determine whether the ADF is ready for a page to be unloaded. If so, return S\_OK. If this command does not apply to the device, return E\_NOTIMPL.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Automatic%20Document%20Feeder%20Commands%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




