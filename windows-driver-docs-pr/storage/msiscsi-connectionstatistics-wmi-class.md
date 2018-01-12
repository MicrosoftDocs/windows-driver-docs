---
title: MSiSCSI\_ConnectionStatistics WMI Class
description: MSiSCSI\_ConnectionStatistics WMI Class
ms.assetid: f12dfa6a-0999-40a3-9e15-bb65dc086911
---

# MSiSCSI\_ConnectionStatistics WMI Class


## <span id="ddk_msiscsi_connectionstatistics_wmi_class_kr"></span><span id="DDK_MSISCSI_CONNECTIONSTATISTICS_WMI_CLASS_KR"></span>


The MSiSCSI\_ConnectionStatistics WMI class expose connection statistics. This class is defined as follows in Iscsiprf.mof.

```
class MSiSCSI_ConnectionStatistics : Win32_PerfRawData {
  [read,key] String  InstanceName;
  [read] boolean  Active;
  [read, WmiDataId(1), WmiVersion(1), 
    cpp_quote(
    "\n    //Text-based identifier for this Initiator that 
    is globally unique.\n"
    "    //The Initiator Name is independent of the location 
    of the initiator.\n"),
    MaxLen(MAX_ISCSI_NAME_LEN)] 
    string  iSCSIName;
  [read, WmiDataId(2), WmiVersion(1), Description("The iSCSI 
    connection ID for this connection instance."): amended] 
    uint16  CID; //session wide namespace
  [read, WmiDataId(3), Description("A uniquely generated 
    session ID used only internally.  Do not mix this with 
    ISID or SSID"): amended,
    cpp_quote(
    "\n    //A uniquely generated session ID used only 
    internally.  Do not mix this with ISID or SSID\n"),
    WmiVersion(1)] 
    uint64  USID;
  [WmiDataId(4), DisplayName("Adapter Id") : amended, 
    DisplayInHex, description("Id that is globally unique to 
    each instance of each adapter. Using the address of the 
    Adapter Extension is a good idea.") : amended]
    uint64  UniqueAdapterId;
  [WmiDataId(5), DisplayName("Bytes Sent"): amended, 
    PerfDefault, CounterType(0x10410400),
    //    32bit per sec display
    DefaultScale(0), PerfDetail(100), read, 
    Description("Count of # of bytes sent over this 
    connection"): amended] 
    uint64  BytesSent;
  [WmiDataId(6), DisplayName("Bytes Received"): amended, 
    PerfDefault, CounterType(0x10410400),
    //    32bit per sec display
    DefaultScale(0), PerfDetail(100), read, 
    Description("Count of # of bytes received over this 
    connection"): amended] 
    uint64  BytesReceived;
  [WmiDataId(7), DisplayName("PDUs Sent"): amended, 
    PerfDefault, CounterType(0x10410400),
    //    32bit per sec display
    DefaultScale(0), PerfDetail(100), read, 
    Description("Count of # of  PDU Commands Sent over this 
    connection"): amended] 
    uint64  PDUCommandsSent;
  [WmiDataId(8), DisplayName("PDUs Received"): amended, 
    PerfDefault, CounterType(0x10410400),
    //    32bit per sec display
    DefaultScale(0), PerfDetail(100), read, 
    Description("Count of # of PDUResponses received over 
    this connection"): amended] 
    uint64  PDUResponsesReceived;
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**MSiSCSI\_ConnectionStatistics**](https://msdn.microsoft.com/library/windows/hardware/ff562986) data structure.

Initiators must register the MSiSCSI\_ConnectionStatistics WMI class with the following target instance name:

```
targetname_#:#
```

The first number sign (\#) is the value in the **USID** member of the [**MSiSCSI\_ConnectionStatistics**](https://msdn.microsoft.com/library/windows/hardware/ff562986) structure, and the second number sign (\#) is the value in the **CID** member of this class.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MSiSCSI_ConnectionStatistics%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




