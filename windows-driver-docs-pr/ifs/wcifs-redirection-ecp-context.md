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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20WCIFS_REDIRECTION_ECP_CONTEXT%20structure%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




