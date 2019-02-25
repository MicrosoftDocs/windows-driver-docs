---
title: Overview of Hyper-V Extensible Switch Policies
description: Overview of Hyper-V Extensible Switch Policies
ms.assetid: 1D0AC55B-60F7-400E-A376-F3E2F7373A92
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of Hyper-V Extensible Switch Policies


The Hyper-V platform and the extensible switch interface provide an infrastructure to manage switch and port policies for an extensible switch. These policies are managed through PowerShell cmdlets and WMI-based application programs. This infrastructure also provides support for the storage and migration of policies.

Independent software vendors (ISVs) can use this infrastructure to register their own custom policies. After they are registered, these policies can be discovered and managed through the built-in Hyper-V policy interfaces. Properties of policies can be configured either on a per-port level or a per-switch level.

In addition to custom policy properties, the Hyper-V extensible switch interface provides the infrastructure to obtain status information for custom policy properties on a per-port or a per-switch basis. This status information is known as *feature status* information.

Extensible switch custom policy data is registered with the WMI management layer by using managed object format (MOF) class definitions. The following shows an example of a MOF class for a custom port policy property.

```C++
#pragma namespace("\\\\.\\root\\virtualization\\v2")

[ Dynamic, 
 UUID("F2F73F23-2B8E-457a-96C4-F541201C9150"),
 ExtensionId("5CBF81BE-5055-47CD-9055-A76B2B4E369E"), 
 Provider("VmmsWmiInstanceAndMethodProvider"), 
 Locale(0x409),
 InterfaceVersion("1"),
 InterfaceRevision("0"),
DisplayName("VendorName Port Settings Friendly Name") : Amended,
Description("VendorName Port Settings detailed description.") : Amended]
class Vendor_SampleFeatureSettingData: Msvm_EthernetSwitchPortFeatureSettingDataMsvm
{
  [WmiDataId(1),
   InterfaceVersion("1"),
   InterfaceRevision("0")]
  uint8  IntValue8 = 0;

  [WmiDataId(2),
   InterfaceVersion("1"),
   InterfaceRevision("0")]
  uint16 IntValue16 = 0;

  [WmiDataId(3),
   InterfaceVersion("1"),
   InterfaceRevision("0")]
  uint32 IntValue32 = 0;

  [WmiDataId(4),
   InterfaceVersion("1"),
   InterfaceRevision("0")]
  uint64 IntValue64 = 0;

  [WmiDataId(5),
   InterfaceVersion("1"),
   InterfaceRevision("0"), 
   MaxLen(255)]
  string FixedLengthString = "";

  [WmiDataId(6),
   InterfaceVersion("1"),
   InterfaceRevision("0")]
  string VariableLengthString = "";

  [WmiDataId(7),
   InterfaceVersion("1"),
   InterfaceRevision("0"),
   Max(8)]
  uint32 FixedLengthArray[] = {};

  [WmiDataId(8),
   InterfaceVersion("1"),
   InterfaceRevision("0")]
  uint32 VariableLengthArray[] = {};

};
```

The WMI management layer serializes the MOF data when it is transferred to an underlying extensible switch extension. The MOF class is serialized to a corresponding C structure that can be processed by the Hyper-V extensible switch extension. The following shows an example of the C structure that was serialized for the MOF class from the previous example.

```C++
#pragma pack(8)

typedef struct _VARIABLE_LENGTH_ARRAY
{
    UINT32 Buffer[1];
} VARIABLE_LENGTH_ARRAY;

typedef struct _SAMPLE_FEATURE_SETTINGS
{
    UINT8  IntValue8;
    UINT32 IntValue16;
    UINT32 IntValue32;
    UINT64 IntValue64;
    UINT16 FixedLengthStringByteCount;
    WCHAR  FixedLengthString[256]; 
    UINT32 VariableLengthStringOffset;    // offset to VARIABLE_LENGTH_STRING structure
    UINT32 FixedLengthArrayElementCount;
    UINT32 FixedLengthArray[8];
    UINT32 VariableLengthArrayElementCount;
    UINT32 VariableLengthArrayOffset;   // offset to VARIABLE_LENGTH_ARRAY
} SAMPLE_FEATURE_SETTINGS;
 
typedef struct _VARIABLE_LENGTH_STRING
{
    USHORT StringLength;
    WCHAR  StringBuffer[1];
} VARIABLE_LENGTH_STRING;
```

This example highlights the following points that occur when a MOF class is serialized to a corresponding C structure for an extensible switch policy property:

-   The version definition in MOF files is converted into a USHORT value, where the high-order bits contain the major version and the low-order bits contain the minor version. The version is serialized by using the following code:

    `  (((MajorVersion) << 8) + (MinorVersion))`

    For example, Version("1") above would be serialized to a value of 0x0100 through `(((1) << 8) + (0))`. Version ("1.1") would be serialized to a value of 0x0101 through `(((1) << 8) + (1))`.

    When a custom policy property is issued to an underlying extension, the **PropertyVersion** member of the structures that define policy properties contains the serialized version value.

    For example, when the extensible switch interface issues an object identifier (OID) request of [OID\_SWITCH\_PORT\_PROPERTY\_ADD](https://msdn.microsoft.com/library/windows/hardware/hh598275), the OID is associated with an [**NDIS\_SWITCH\_PORT\_PROPERTY\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh598238) structure. The **PropertyVersion** member of that structure contains the serialized version value.

-   All variable-length strings are serialized into offsets within the buffer that contains the serialized C structure. Each variable-length string is formatted as a **VARIABLE\_LENGTH\_STRING** structure within this buffer offset.

 

 





