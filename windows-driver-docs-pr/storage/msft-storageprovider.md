---
title: MSFT\_StorageProvider class
description: Represents a storage management provider (SMP) package that manages a storage subsystem.
ms.assetid: afafd4d5-c0c1-4461-814d-bf00de403b3f
keywords:
- MSFT_StorageProvider class Windows Storage Management API
- MSFT_StorageProvider class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageProvider
- MSFT_StorageProvider.Type
- MSFT_StorageProvider.Name
- MSFT_StorageProvider.Manufacturer
- MSFT_StorageProvider.Version
- MSFT_StorageProvider.CimServerName
- MSFT_StorageProvider.URI
- MSFT_StorageProvider.URI_IP
- MSFT_StorageProvider.RemoteSubsystemCacheMode
- MSFT_StorageProvider.SupportsSubsystemRegistration
- MSFT_StorageProvider.SupportedRemoteSubsystemCacheModes
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StorageProvider class

Represents a storage management provider (SMP) package that manages a storage subsystem.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_StorageProvider : MSFT_StorageObject
{
  UInt16  Type;
  String  Name;
  String  Manufacturer;
  String  Version;
  String  CimServerName;
  String  URI;
  String  URI_IP;
  UInt16  RemoteSubsystemCacheMode;
  Boolean SupportsSubsystemRegistration;
  UInt16  SupportedRemoteSubsystemCacheModes;
};
```

## Members

The **MSFT\_StorageProvider** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_StorageProvider** class has these methods.



| Method                                                                      | Description                                                                                                |
|:----------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------|
| [**Discover**](discover-msft-storageprovider.md)                           | Discovers the objects that are owned by the storage provider.                                   |
| [**GetSecurityDescriptor**](msft-storageprovider-getsecuritydescriptor.md) | Retrieves the security descriptor that controls access to the storage provider object instance. |
| [**RegisterSubsystem**](msft-storageprovider-registersubsystem.md)         | Registers a subsystem to be managed by this provider.                                           |
| [**SetAttributes**](msft-storageprovider-setattributes.md)                 | Sets the attributes of the provider.                                                            |
| [**SetSecurityDescriptor**](setsecuritydescriptor-msft-storageprovider.md) | Sets the security descriptor that controls access to the storage provider object instance.      |
| [**UnregisterSubsystem**](msft-storageprovider-unregistersubsystem.md)     | Unregisters a subsystem.                                                                        |



 

### Properties

The **MSFT\_StorageProvider** class has these properties.

 

**CimServerName**
   

Data type: **String**
 

Access type: Read-only
 

If the **Type** property is **SMI-S**, this property contains the name of the CIM Server to be displayed in the user interface. For example, "ACME CIM Server". This property is required to support the SLP discovery mechanism.

If the **Type** property is not **SMI-S**, this property is **NULL**.

 

**Manufacturer**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The name of the manufacturer of the SMP software.

 

**Name**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

A user-friendly name for the storage provider.

 

**RemoteSubsystemCacheMode**
   

Data type: **UInt16**
 

Access type: Read-only
 

The caching mode of this provider.



| Value                                                                                                | Meaning                     |
|------------------------------------------------------------------------------------------------------|-----------------------------|
| <span id="0"></span> **0**  | Unknown          |
| <span id="2"></span> **2**  | Disabled         |
| <span id="3"></span> **3**  | Manual-Discovery |



 

 

**SupportedRemoteSubsystemCacheModes**
   

Data type: **UInt16**
 

Access type: Read-only
 

The caching modes that this provider supports.



| Value                                                                                                | Meaning                     |
|------------------------------------------------------------------------------------------------------|-----------------------------|
| <span id="0"></span> **0**  | Unknown          |
| <span id="2"></span> **2**  | Disabled         |
| <span id="3"></span> **3**  | Manual-Discovery |



 

 

**SupportsSubsystemRegistration**
   

Data type: **Boolean**
 

Access type: Read-only
 

**TRUE** if this provider supports remote registration and management; **FALSE** if it does not.

 

**Type**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

Indicates whether the provider is implemented using SMI-S standard interfaces or SMP WMI interfaces.



| Value                                                                                                                                                                                        | Meaning                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| <span id="SMP"></span><span id="smp"></span> **SMP** 1         | The provider is a native SMP-based provider.                                                                 |
| <span id="SMI-S"></span><span id="smi-s"></span> **SMI-S** 2   | The provider is an SMI-S-based provider that is visible through the SMI-S proxy storage management provider. |



 

 

**URI**
   

Data type: **String**
 

Access type: Read-only
 

If the **Type** property is **SMI-S**, this property contains the protocol, host name, and port that connect to an SMI-S server.

If the **Type** property is not **SMI-S**, this property is **NULL**.

 

**URI\_IP**
   

Data type: **String**
 

Access type: Read-only
 

If the **Type** property is **SMI-S**, this property contains the protocol, IP address, and port that connect to an SMI-S server. This pro

If the **Type** property is not **SMI-S**, this property is **NULL**.

 

**Version**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

A free-form version string used by the SMP manufacturer to differentiate between software versions.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



 

