---
title: MSiSCSI\_InitiatorSessionInfo WMI Class
description: MSiSCSI\_InitiatorSessionInfo WMI Class
ms.assetid: 73053af8-80b0-4cab-8e27-c651be8f0e8c
---

# MSiSCSI\_InitiatorSessionInfo WMI Class


## <span id="ddk_msiscsi_initiatorsessioninfo_wmi_class_kr"></span><span id="DDK_MSISCSI_INITIATORSESSIONINFO_WMI_CLASS_KR"></span>


The MSiSCSI\_InitiatorSessionInfo WMI class exposes information that is associated with the sessions and collections that belong to the indicated HBA initiator.

Because this class is associated with a particular instance of a storage miniport driver, the miniport driver must register the class using the name of the particular physical device object (PDO) that the miniport driver manages.

The MSiSCSI\_InitiatorSessionInfo class is defined in *Mgmt.mof*.

```
class MSiSCSI_InitiatorSessionInfo {
  [read,key] String  InstanceName;
  [read] boolean  Active;
  [WmiDataId(1), DisplayName("Adapter Id") : amended, 
    DisplayInHex, description("Id that is globally unique to
    each instance of each adapter. Using the address of the 
    Adapter Extension is a good idea.") : amended]
    uint64  UniqueAdapterId;
  [WmiDataId(2), read, DisplayName("Count of Elements in 
    SessionsList array") : amended,
    cpp_quote(
    "\n    // Number of elements in SessionList array\n"),
    Description("Number of elements in SessionList array") : 
    amended] 
    uint32  SessionCount;
  [WmiDataId(3), read, DisplayName("List Of Sessions") :
    amended, Description("Variable length array of sessions.
    SessionCount specifies the number of elements in the 
    array") : amended, WmiSizeIs("SessionCount")]  
    ISCSI_SessionStaticInfo  SessionsList[];
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**MSiSCSI\_InitiatorSessionInfo**](https://msdn.microsoft.com/library/windows/hardware/ff563054) data structure.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MSiSCSI_InitiatorSessionInfo%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




