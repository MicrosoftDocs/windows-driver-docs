---
title: HBA\_STATUS
description: HBA\_STATUS
ms.assetid: 2fabfa86-7f8a-4c90-8aa0-53e42bd5c075
---

# HBA\_STATUS


## <span id="ddk_hba_status_kr"></span><span id="DDK_HBA_STATUS_KR"></span>


The HBA\_STATUS WMI class qualifier indicates the result of a WMI request that was made to a WMI provider HBA.

The following table lists the qualifier names and the meaning of each name:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Qualifier</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>HBA_STATUS_OK</p></td>
<td align="left"><p>No errors detected on the HBA.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HBA_STATUS_ERROR</p></td>
<td align="left"><p>Error detected on the HBA.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HBA_STATUS_ERROR_NOT_SUPPORTED</p></td>
<td align="left"><p>Function not supported.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HBA_STATUS_ERROR_INVALID_HANDLE</p></td>
<td align="left"><p>Invalid handle.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HBA_STATUS_ERROR_ARG</p></td>
<td align="left"><p>Bad argument.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HBA_STATUS_ERROR_ILLEGAL_WWN</p></td>
<td align="left"><p>Worldwide name not recognized. For information concerning worldwide names, see the T11 committee's <em>Fibre Channel HBA API</em> specification.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HBA_STATUS_ERROR_ILLEGAL_INDEX</p></td>
<td align="left"><p>Index not recognized.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HBA_STATUS_ERROR_MORE_DATA</p></td>
<td align="left"><p>Larger buffer required.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HBA_STATUS_ERROR_STALE_DATA</p></td>
<td align="left"><p>Information has changed since the last refresh operation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HBA_STATUS_SCSI_CHECK_CONDITION</p></td>
<td align="left"><p>SCSI Check Condition reported.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HBA_STATUS_ERROR_BUSY</p></td>
<td align="left"><p>Adapter busy or reserved, retry might be required.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HBA_STATUS_ERROR_TRY_AGAIN</p></td>
<td align="left"><p>Request timed out, retry might be required.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HBA_STATUS_ERROR_UNAVAILABLE</p></td>
<td align="left"><p>Referenced HBA has been removed or deactivated.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HBA_STATUS_ERROR_ELS_REJECT</p></td>
<td align="left"><p>The requested ELS was rejected by the local adapter.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HBA_STATUS_ERROR_INVALID_LUN</p></td>
<td align="left"><p>The specified LUN is not provided by the specified adapter.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HBA_STATUS_ERROR_INCOMPATIBLE</p></td>
<td align="left"><p>An incompatibility has been detected. Library and driver modules might have implemented different versions of the HBA API specification.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HBA_STATUS_ERROR_AMBIGUOUS_WWN</p></td>
<td align="left"><p>Multiple adapters have a matching worldwide name (WWN). This could occur if the NodeWWN of multiple adapters is identical. For information concerning worldwide names in general and NodeWWN in particular, see the T11 committee's <em>Fibre Channel HBA API</em> specification.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HBA_STATUS_ERROR_LOCAL_BUS</p></td>
<td align="left"><p>A persistent binding request included a bad local SCSI bus number.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HBA_STATUS_ERROR_LOCAL_TARGET</p></td>
<td align="left"><p>A persistent binding request included a bad local SCSI target number.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HBA_STATUS_ERROR_LOCAL_LUN</p></td>
<td align="left"><p>A persistent binding request included a bad local SCSI LUN.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HBA_STATUS_ERROR_LOCAL_SCSIID_BOUND</p></td>
<td align="left"><p>A persistent binding set request included a local SCSI ID that was already bound.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HBA_STATUS_ERROR_TARGET_FCID</p></td>
<td align="left"><p>A persistent binding request included an invalid FCP target FCID. For a definition of an FCP target FCID, see the T11 committee's <em>Fibre Channel HBA API</em> specification.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HBA_STATUS_ERROR_TARGET_NODE_WWN</p></td>
<td align="left"><p>A persistent binding request included a bad FCP target node WWN.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HBA_STATUS_ERROR_TARGET_PORT_WWN</p></td>
<td align="left"><p>A persistent binding request included a bad FCP target port WWN.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HBA_STATUS_ERROR_TARGET_LUN</p></td>
<td align="left"><p>A persistent binding request included an FCP LUN that the target does not recognize.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HBA_STATUS_ERROR_TARGET_LUID</p></td>
<td align="left"><p>A persistent binding request contained an undefined or otherwise inaccessible logical unit unique identifier.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HBA_STATUS_ERROR_NO_SUCH_BINDING</p></td>
<td align="left"><p>A persistent binding remove request contained a binding which did not match a binding established by the specified port.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HBA_STATUS_ERROR_NOT_A_TARGET</p></td>
<td align="left"><p>A SCSI command was sent to an Nx_Port that was not a SCSI target port. For a definition of Nx_Port, see the T11 committee's <em>Fibre Channel HBA API</em> specification.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HBA_STATUS_ERROR_UNSUPPORTED_FC4</p></td>
<td align="left"><p>A request was made concerning an unsupported FC-4 protocol. For an explanation of the FC-4 protocol, see the T11 committee's <em>Fibre Channel HBA API</em> specification.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HBA_STATUS_ERROR_INCAPABLE</p></td>
<td align="left"><p>A request was made to enable unimplemented capabilities for a port.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HBA_STATUS_ERROR_TARGET_BUSY</p></td>
<td align="left"><p>Executing the requested SCSI command would cause a SCSI overlapped command condition.</p></td>
</tr>
</tbody>
</table>

 

By including *Hbaapi.h* your software will have access to a series of symbolic constants that correspond to the type names in the previous table. The definitions for these symbolic constants are not included in *Hbapiwmi.h* (the file that the WMI tool suite generates when it compiles).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20HBA_STATUS%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




