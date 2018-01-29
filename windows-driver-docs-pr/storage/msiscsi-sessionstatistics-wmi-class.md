---
title: MSiSCSI\_SessionStatistics WMI Class
description: MSiSCSI\_SessionStatistics WMI Class
ms.assetid: fc9afa1b-dad3-4f3d-9fe2-e37d402f7bef
---

# MSiSCSI\_SessionStatistics WMI Class


## <span id="ddk_msiscsi_sessionstatistics_wmi_class_kr"></span><span id="DDK_MSISCSI_SESSIONSTATISTICS_WMI_CLASS_KR"></span>


The MSiSCSI\_SessionStatistics WMI class exposes session statistics.

The MSiSCSI\_SessionStatistics class is defined in Iscsiprf.mof.

```
class MSiSCSI_SessionStatistics : Win32_PerfRawData {
  [read,key] String  InstanceName;
  [read] boolean Active;
  [read, WmiDataId(1), WmiVersion(1), 
    cpp_quote(
    "\n    //Text-based identifier for this Initiator that 
    is globally unique.\n"
    "    //The Initiator Name is independent of the location 
    of the initiator.\n"),
    MaxLen(MAX_ISCSI_NAME_LEN)] 
    string  iSCSIName;
  [read, WmiDataId(2), Description("A uniquely generated 
    session ID used only internally.  Do not mix this with 
    ISID or SSID"): amended, 
    cpp_quote(
    "\n    //A uniquely generated session ID used only 
    internally.  Do not mix this with ISID or SSID\n"),
    WmiVersion(1)] 
    uint64  USID;
  [WmiDataId(3), DisplayName("Adapter Id") : amended, 
    DisplayInHex, description("Id that is globally unique to 
    each instance of each adapter. Using the address of the 
    Adapter Extension is a good idea.") : amended]
    uint64  UniqueAdapterId;
  [WmiDataId(4), DisplayName("Bytes Sent"): amended, 
    PerfDefault, CounterType(0x10410400),
    //    32bit per sec display
    DefaultScale(0), PerfDetail(100), read, 
    Description("Number of bytes sent per second over this 
    session"): amended] 
    uint64  BytesSent;
  [WmiDataId(5), DisplayName("Bytes Received"): amended, 
    PerfDefault, CounterType(0x10410400),
    //    32bit per sec display
    DefaultScale(0), PerfDetail(100), read, 
    Description("Number of bytes per second received over 
    this session"): amended] 
    uint64  BytesReceived;
  [WmiDataId(6), DisplayName("PDUs Sent"): amended, 
    PerfDefault, CounterType(0x10410400),
    //    32bit per sec display
    DefaultScale(0), PerfDetail(100), read, 
    Description("Number of PDU Commands per second sent over 
    this session"): amended] 
    uint64  PDUCommandsSent;
  [WmiDataId(7), DisplayName("PDUs Received"): amended, 
    PerfDefault, CounterType(0x10410400),
    //    32bit per sec display
    DefaultScale(0), PerfDetail(100), read, 
    Description("Number of PDUResponses per second received 
    over this session"): amended] 
    uint64  PDUResponsesReceived;
  [WmiDataId(8), DisplayName("Digest Errors"): amended, 
    PerfDefault, CounterType(0x00010000),
    //    PERF_COUNTER_RAWCOUNT
    DefaultScale(0), PerfDetail(100), read, 
    Description("Count of Number of Digest errors occurred in 
    this session"): amended] 
    uint64  DigestErrors;
  [WmiDataId(9), DisplayName("ConnectionTimeout Errors"): 
    amended, PerfDefault, CounterType(0x00010000),
    //    PERF_COUNTER_RAWCOUNT
    DefaultScale(0), PerfDetail(100), read, 
    Description("Count of Number of ConnectionTimeout errors 
    occurred in this session"): amended] 
    uint64  ConnectionTimeoutErrors;
  [WmiDataId(10), DisplayName("Format Errors"): amended, 
    PerfDefault, CounterType(0x00010000),
    //    PERF_COUNTER_RAWCOUNT
    DefaultScale(0), PerfDetail(100), read, 
    Description("Count of Number of Format errors occurred in 
    this session"): amended] 
    uint64  FormatErrors;
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**MSiSCSI\_SessionStatistics**](https://msdn.microsoft.com/library/windows/hardware/ff563137) data structure.

Initiators must register the MSiSCSI\_SessionStatistics class with the following dynamic instance name for the session:

```
targetname_#
```

The number sign (\#) is the value in the **USID** member of this class.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MSiSCSI_SessionStatistics%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




