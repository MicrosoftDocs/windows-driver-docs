---
title: WCIFS\_REDIRECTION\_ECP\_CONTEXT structure
description: Describes the redirection state of a file for a specific create operation.
ms.assetid: 6101490D-54B9-4A34-ADB5-9CC2B855691D
keywords: ["WCIFS_REDIRECTION_ECP_CONTEXT structure Installable File System Drivers", "PWCIFS_REDIRECTION_ECP_CONTEXT structure pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- WCIFS_REDIRECTION_ECP_CONTEXT
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WCIFS\_REDIRECTION\_ECP\_CONTEXT structure


Describes the redirection state of a file for a specific create operation.

Syntax
------

```ManagedCPlusPlus
typedef struct _WCIFS_REDIRECTION_ECP_CONTEXT {
  USHORT      Size;
  USHORT      Flags;
  FILE_ID_128 FileId;
  GUID        VolumeGuid;
} WCIFS_REDIRECTION_ECP_CONTEXT, *PWCIFS_REDIRECTION_ECP_CONTEXT;
```

Members
-------

**Size**  
The size of the structure, `sizeof(WCIFS_REDIRECTION_ECP_CONTEXT)`.

**Flags**  
Indicates the redirection state of a file.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><a href="" id="wcifs-redirection-flags-create-serviced-from-layer"></a>
<strong>WCIFS_REDIRECTION_FLAGS_CREATE_SERVICED_FROM_LAYER</strong>
0x0001</td>
<td align="left"><p>This is a redirected file from a layer that is not registered in the LayerRootLocations registry key.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="" id="wcifs-redirection-flags-create-serviced-from-scratch"></a>
<strong>WCIFS_REDIRECTION_FLAGS_CREATE_SERVICED_FROM_SCRATCH</strong>
0x0002</td>
<td align="left"><p>This is a new or modified file, it is not redirected.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="" id="wcifs-redirection-flags-create-serviced-from-registered-layer"></a>
<strong>WCIFS_REDIRECTION_FLAGS_CREATE_SERVICED_FROM_REGISTERED_LAYER</strong>
0x0004</td>
<td align="left"><p>This is a redirected file from a layer that is listed in the LayerRootLocations registry key.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="" id="wcifs-redirection-flags-create-serviced-from-remote-layer"></a>
<strong>WCIFS_REDIRECTION_FLAGS_CREATE_SERVICED_FROM_REMOTE_LAYER</strong>
0x0008</td>
<td align="left"><p>This is a redirected file from a remote file system relative to the container. It may or may not be registered as a layer on that server. For Hyper-V containers, the remote server is the host of the Hyper-V container utility VM.</p></td>
</tr>
</tbody>
</table>

 

**FileId**  
The identifier of the backing file.

**VolumeGuid**  
The GUID-based identifier of the disk volume where the backing file resides.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 10, version 1607</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ntifs.h</td>
</tr>
</tbody>
</table>

 

 





