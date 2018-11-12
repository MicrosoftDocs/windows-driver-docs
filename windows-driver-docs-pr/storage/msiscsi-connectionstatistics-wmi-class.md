---
title: MSiSCSI\_ConnectionStatistics WMI Class
description: MSiSCSI\_ConnectionStatistics WMI Class
ms.assetid: f12dfa6a-0999-40a3-9e15-bb65dc086911
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSiSCSI\_ConnectionStatistics WMI Class


## <span id="ddk_msiscsi_connectionstatistics_wmi_class_kr"></span><span id="DDK_MSISCSI_CONNECTIONSTATISTICS_WMI_CLASS_KR"></span>


The MSiSCSI\_ConnectionStatistics WMI class expose connection statistics. This class is defined as follows in Iscsiprf.mof.

```cpp
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

```cpp
targetname_#:#
```

The first number sign (\#) is the value in the **USID** member of the [**MSiSCSI\_ConnectionStatistics**](https://msdn.microsoft.com/library/windows/hardware/ff562986) structure, and the second number sign (\#) is the value in the **CID** member of this class.

 

 





