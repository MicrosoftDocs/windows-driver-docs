---
title: Handling the OID_SWITCH_NIC_SAVE Request
description: Handling the OID_SWITCH_NIC_SAVE Request
ms.assetid: 42D66822-6F7E-4772-A280-7823BC29FD71
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling the OID\_SWITCH\_NIC\_SAVE Request


When a Hyper-V child partition with a network adapter connection to an extensible switch port is stopped or its state is saved, the Hyper-V extensible switch interface is notified. This causes the protocol edge of the extensible switch to issue an object identifier (OID) method request of [OID\_SWITCH\_NIC\_SAVE](https://msdn.microsoft.com/library/windows/hardware/hh598268) down the extensible switch driver stack. When an extensible switch extension receives this OID request, it can save its run-time data for the specified network adapter connection that is attached to the child partition.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure for the [OID\_SWITCH\_NIC\_SAVE](https://msdn.microsoft.com/library/windows/hardware/hh598268) request contains a pointer to an [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216) structure. This structure is allocated by the protocol edge of the extensible switch and initialized in the following way:

-   The **Header** member is initialized to contain the current type, revisionof the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216) structure. Size is set to the full buffer size.

-   The **PortId** member contains the unique identifier of the extensible switch port for which the save operation is being performed.

When it receives the [OID\_SWITCH\_NIC\_SAVE](https://msdn.microsoft.com/library/windows/hardware/hh598268) method request, the extension does the following:

1.  The extension reads the **PortId** member of the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216) structure.

2.  If the extension has run-time data to save for the specified NIC, it saves its data within the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216) structure starting with *SaveDataOffset* bytes from the start of the structure. The extension then completes the OID method request with NDIS\_STATUS\_SUCCESS.

3.  If the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216) structure does not provide a sufficient buffer to hold the runtime state, the extension the extension sets the method structure’s *BytesNeeded* field to **NDIS\_SIZEOF\_NDIS\_SWITCH\_NIC\_SAVE\_STATE\_REVISION\_1** plus the amount of buffer necessary to hold the save data, and completes the OID with **NDIS\_STATUS\_BUFFER\_TOO\_SHORT**. The OID will be re-issued with the required size.

4.  If the extension does not have run-time data to save for the specified NIC, it must call [**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830). This forwards the OID method request to underlying drivers in the extensible switch driver stack. For more information about this procedure, see [Filtering OID Requests in an NDIS Filter Driver](filtering-oid-requests-in-an-ndis-filter-driver.md).

If the extension has run-time port data to save, it must follow these guidelines when it saves run-time port data within the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216) structure:

1.  The extension sets the **ExtensionId** member to the GUID value that uniquely identifies the driver.
2.  The extension sets the **ExtensionFriendlyName** member to the name of the driver.

    **Note**  The NDIS\_SWITCH\_EXTENSION\_FRIENDLYNAME data type is type-defined by the [**IF\_COUNTED\_STRING**](https://msdn.microsoft.com/library/windows/hardware/hh451419) structure. A string that is defined by this structure does not have to be null-terminated. However, the length of the string must be set in the **Length** member of this structure. If the string is NULL-terminated, the **Length** member must not include the terminating NULL character.

     

3.  If a feature class is associated with the saved run-time data, the extension sets the **FeatureClassId** with the GUID that uniquely identifies the class.

    **Note**  If a feature class is not associated with the saved run-time data, the extension sets the **FeatureClassId** to zero.

     

4.  The extension copies the run-time data to the **SaveData** member and sets the **SaveDataSize** member to the size, in bytes, of the run-time data.

**Note**  The extension must not change the **Header** or **PortId** members of the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216) structure.

 

OID method requests of [OID\_SWITCH\_NIC\_SAVE](https://msdn.microsoft.com/library/windows/hardware/hh598268) are ultimately handled by the underlying miniport edge of the extensible switch. Once this OID method request has been forwarded to the miniport driver through the extensible switch driver stack, the miniport driver completes the OID request with NDIS\_STATUS\_SUCCESS. This notifies the protocol edge of the extensible switch that all extensions in the extensible switch driver stack have been queried for run-time port data. The protocol edge of the extensible switch then issues an OID set request of [OID\_SWITCH\_NIC\_SAVE\_COMPLETE](https://msdn.microsoft.com/library/windows/hardware/hh598269) to complete the save operation.

 

 





