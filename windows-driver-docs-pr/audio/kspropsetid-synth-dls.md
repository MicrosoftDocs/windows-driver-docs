---
title: KSPROPSETID\_Synth\_Dls
description: KSPROPSETID\_Synth\_Dls
ms.assetid: 8d6038bf-1ec4-4120-9815-d1e6b7994f33
keywords: ["KSPROPSETID_Synth_Dls"]
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPSETID\_Synth\_Dls


## <span id="ddk_kspropsetid_synth_dls_ks"></span><span id="DDK_KSPROPSETID_SYNTH_DLS_KS"></span>


The `KSPROPSETID_Synth_Dls` property set contains properties that are used to download DLS samples and instruments to a MIDI synthesizer. These are the properties of a synth node ([**KSNODETYPE\_SYNTHESIZER**](ksnodetype-synthesizer.md)) on a DirectMusic pin of a DirectMusic filter (see [MIDI and DirectMusic Filters](https://msdn.microsoft.com/library/windows/hardware/ff537520)).

This section describes the behavior of these properties with regard to how they download and unload "chunks" of memory containing DLS data. The actual format of the downloaded instrument and wave data chunks is specified in the low-level DLS discussion in the Microsoft Windows SDK documentation.

DLS downloads and unloads can occur at any time during the pin's existence. Unlike DirectMusic events, they are not time-stamped and should be processed as soon as possible.

In this section, the term DLS resource, or just resource, refers to either a DLS instrument chunk or a DLS wave chunk. The system properly maintains reference counts on all DLS resources:

-   When a client unloads the last instrument referencing a wave, the system automatically generates a call to unload the wave.

-   Conversely, the system defers the call to unload a wave until the client unloads the last instrument referencing the wave.

Property items in this set are specified by KSPROPERTY\_SYNTH\_DLS enumeration values, as defined in header file Dmusprop.h.

## <span id="ddk_ksproperty_synth_dls_append_ks"></span><span id="DDK_KSPROPERTY_SYNTH_DLS_APPEND_KS"></span>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

The KSPROPERTY\_SYNTH\_DLS\_APPEND property specifies the amount of reserved storage space that the client appends to the DLS data in each buffer that it downloads to the synthesizer.

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
<th align="left">Get</th>
<th align="left">Set</th>
<th align="left">Target</th>
<th align="left">Property descriptor type</th>
<th align="left">Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Yes</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Pin</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537143" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537143)"><strong>KSNODEPROPERTY</strong></a></p></td>
<td align="left"><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type ULONG and specifies the number of bytes that the miniport driver needs to reserve for its own use at the end of each downloaded DLS data buffer. The client then allocates each download buffer to be large enough to contain the requested number of bytes after the end of the downloaded data.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_SYNTH\_DLS\_APPEND property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code. The following table shows some of the possible error codes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Status Code</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>STATUS_UNSUCCESSFUL</p></td>
<td align="left"><p>The operation did not complete successfully.</p></td>
</tr>
</tbody>
</table>

 

These additional bytes are intended for drivers that need extra padding for alignment requirements or to replicate the start of a sample in order to simplify sample interpolation.

## <span id="ddk_ksproperty_synth_dls_compact_ks"></span><span id="DDK_KSPROPERTY_SYNTH_DLS_COMPACT_KS"></span>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

The KSPROPERTY\_SYNTH\_DLS\_COMPACT property is a request for the synthesizer to make available the largest possible chunk of free sample memory.

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
<th align="left">Get</th>
<th align="left">Set</th>
<th align="left">Target</th>
<th align="left">Property descriptor type</th>
<th align="left">Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>No</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Pin</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537143" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537143)"><strong>KSNODEPROPERTY</strong></a></p></td>
<td align="left"><p>None</p></td>
</tr>
</tbody>
</table>

 

No property value (operation data) is associated with this property.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_SYNTH\_DLS\_COMPACT property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code. The following table shows some of the possible error codes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Status Code</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>STATUS_UNSUCCESSFUL</p></td>
<td align="left"><p>The operation did not complete successfully.</p></td>
</tr>
</tbody>
</table>

 

The implementation of the handler for this property should not interrupt playback.

For more information, see the description of the **IDirectMusicPort::Compact** method in the Microsoft Windows SDK documentation.

## <span id="ddk_ksproperty_synth_dls_download_ks"></span><span id="DDK_KSPROPERTY_SYNTH_DLS_DOWNLOAD_KS"></span>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

The KSPROPERTY\_SYNTH\_DLS\_DOWNLOAD property is used to download DLS data to the synthesizer.

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
<th align="left">Get</th>
<th align="left">Set</th>
<th align="left">Target</th>
<th align="left">Property descriptor type</th>
<th align="left">Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Yes</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Pin</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537143" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537143)"><strong>KSNODEPROPERTY</strong></a> + <a href="https://msdn.microsoft.com/library/windows/hardware/ff538460" data-raw-source="[&lt;strong&gt;SYNTH_BUFFER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff538460)"><strong>SYNTH_BUFFER</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff538429" data-raw-source="[&lt;strong&gt;SYNTHDOWNLOAD&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff538429)"><strong>SYNTHDOWNLOAD</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property descriptor (instance data) consists of a KSNODEPROPERTY structure that is immediately followed by a SYNTH\_BUFFER structure, which specifies the location and size of the DLS data buffer that is being downloaded.

The property value (operation data) is a SYNTHDOWNLOAD structure. The miniport driver passes back the following information in this structure:

-   A handle that the miniport driver generates to uniquely identify the downloaded DLS data. This client should save this handle and use it later to unload the data (see [**KSPROPERTY\_SYNTH\_DLS\_UNLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff537398)).

-   A Boolean value that indicates whether the client can free the buffer containing the DLS data after the property request completes. If the miniport driver has made its own copy of the DLS data, the client can free the buffer. Otherwise, if the miniport driver continues to use the client's original DLS data buffer, the client should not free the buffer until the miniport driver unloads the DLS data.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_SYNTH\_DLS\_DOWNLOAD property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code. The following table shows some of the possible error codes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Status Code</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>STATUS_BUFFER_TOO_SMALL</p></td>
<td align="left"><p>The buffer was too small to complete the operation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_UNSUCCESSFUL</p></td>
<td align="left"><p>The operation did not complete successfully.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_NO_MEMORY</p></td>
<td align="left"><p>No memory is available to complete this request.</p></td>
</tr>
</tbody>
</table>

 

For more information, see the discussion of the **IDirectMusicPort::DownloadInstrument** method in the Microsoft Windows SDK documentation.

**Example**

The KSPROPERTY\_SYNTH\_DLS\_DOWNLOAD property request specifies the location of the DLS download data with a user memory address. The miniport driver should probe and lock the user memory containing the DLS data before attempting to access it. The following example code shows how to do this:

```cpp
  NTSTATUS Status = STATUS_UNSUCCESSFUL;
  PSYNTH_BUFFER pDlsBuffer = (PSYNTH_BUFFER)pRequest->Instance;
  PMDL pMdl = IoAllocateMdl(pDlsBuffer->BufferAddress, pDlsBuffer->BufferSize,
                            FALSE, FALSE, NULL);
  if (pMdl)
  {
      __try
      {
          MmProbeAndLockPages(pMdl, KernelMode, IoReadAccess);
          PVOID pvUserData = MmGetSystemAddressForMdlSafe(pMdl, NormalPagePriority);
 
         // do something with the data here
      }
      __except (EXCEPTION_EXECUTE_HANDLER)
      {
          Status = GetExceptionCode();
      }
 
      MmUnlockPages(pMdl);
      IoFreeMdl(pMdl);
  }
  else
  {
      Status = STATUS_NO_MEMORY;
  }
```

## <span id="ddk_ksproperty_synth_dls_unload_ks"></span><span id="DDK_KSPROPERTY_SYNTH_DLS_UNLOAD_KS"></span>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

The KSPROPERTY\_SYNTH\_DLS\_UNLOAD property unloads a DLS data resource that was previously downloaded.

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
<th align="left">Get</th>
<th align="left">Set</th>
<th align="left">Target</th>
<th align="left">Property descriptor type</th>
<th align="left">Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>No</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Pin</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537143" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537143)"><strong>KSNODEPROPERTY</strong></a></p></td>
<td align="left"><p>HANDLE</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type HANDLE and contains the handle of the downloaded DLS data resource that is to be freed. This is the handle that the miniport driver generated to identify the DLS data in a previous [**KSPROPERTY\_SYNTH\_DLS\_DOWNLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff537396)get-property request.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_SYNTH\_DLS\_UNLOAD property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code. The following table shows some of the possible error codes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Status Code</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>STATUS_BUFFER_TOO_SMALL</p></td>
<td align="left"><p>The buffer was too small to complete the operation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_UNSUCCESSFUL</p></td>
<td align="left"><p>The operation did not complete successfully.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_PENDING</p></td>
<td align="left"><p>The operation will complete at a later time.</p></td>
</tr>
</tbody>
</table>

 

The miniport driver should unload the DLS data as soon as there are no notes playing that use the DLS data. If the synthesizer is not able to free the memory associated with the DLS data resource at the time of the KSPROPERTY\_SYNTH\_DLS\_UNLOAD set-property request, it can use asynchronous property completion to finish the request at a later time.

If, after unloading the DLS data resource, the synthesizer receives a note-on event that uses the resource, the miniport driver should ignore the event unless a new DLS data resource has been downloaded in the interim.

For more information, see the discussion of the **IDirectMusicPort::UnloadInstrument** method in the Microsoft Windows SDK documentation.

## <span id="ddk_ksproperty_synth_dls_waveformat_ks"></span><span id="DDK_KSPROPERTY_SYNTH_DLS_WAVEFORMAT_KS"></span>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

The KSPROPERTY\_SYNTH\_DLS\_WAVEFORMAT property is used to query the synthesizer for its output wave format.

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
<th align="left">Get</th>
<th align="left">Set</th>
<th align="left">Target</th>
<th align="left">Property descriptor type</th>
<th align="left">Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Yes</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Pin</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537143" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537143)"><strong>KSNODEPROPERTY</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff538799" data-raw-source="[&lt;strong&gt;WAVEFORMATEX&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff538799)"><strong>WAVEFORMATEX</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type WAVEFORMATEX and specifies the wave format of the synthesizer's output stream.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_SYNTH\_DLS\_WAVEFORMAT property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code. The following table shows some of the possible error codes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Status Code</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>STATUS_BUFFER_TOO_SMALL</p></td>
<td align="left"><p>The buffer was too small to complete the operation.</p></td>
</tr>
</tbody>
</table>

 

A property-value buffer of **sizeof**(WAVEFORMATEX) bytes might not be large enough for all wave formats. For example, a multichannel format requires a buffer of **sizeof**([**WAVEFORMATEXTENSIBLE**](https://msdn.microsoft.com/library/windows/hardware/ff538802)) bytes. If the property request returns a status code of STATUS\_BUFFER\_TOO\_SMALL, the client can check the property-value size that the miniport driver outputs, allocate a larger buffer, and then submit a second request.

For more information, see the description of the **IDirectMusicPort::GetFormat** method in the Microsoft Windows SDK documentation.

 

 





