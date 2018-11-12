---
title: MSiSCSI\_HBASessionConfig WMI Class
description: MSiSCSI\_HBASessionConfig WMI Class
ms.assetid: ef3ac7d0-be4a-457e-b837-a6434776dfc1
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSiSCSI\_HBASessionConfig WMI Class


## <span id="ddk_msiscsi_hbasessionconfig_wmi_class_kr"></span><span id="DDK_MSISCSI_HBASESSIONCONFIG_WMI_CLASS_KR"></span>


Management applications can use the MSiSCSI\_HBASessionConfig WMI class to retrieve and set the default configuration options that a particular instance of a storage miniport driver uses to establish a logon session with a target device.

Because this class is associated with a particular instance of a storage miniport driver, the miniport driver must register the class using the name of the particular physical device object (PDO) that the miniport driver manages.

The MSiSCSI\_HBASessionConfig class is defined as follows in *Mgmt.mof*.

```cpp
class MSiSCSI_HBASessionConfig {
  [key] string  InstanceName;
  boolean  Active;
  [WmiDataId(1), read, write, Description(" The InitialR2T
    key is used to turn off the default use of R2T, thus
    allowing an initiator to start sending data to a target
    as if it has received an initial R2T with Buffer
    Offset=0 and Desired Data Transfer Length=min
    (FirstBurstSize, Expected Data Transfer Length).") :
    amended] 
    boolean  InitialR2T;
  [WmiDataId(2), read, write, Description("The initiator and
    target negotiate support for immediate data. To turn
    immediate data off, the initiator or target must state
    its desire to do so.  ImmediateData can be turned on if
    both the initiator and target have ImmediateData=Yes.")
    : amended]
    boolean  ImmediateData;
  [WmiDataId(3), read, write, Description("Maximum data
    segment length in bytes they can receive in an iSCSI
    PDU.") : amended] 
    uint32  MaxRecvDataSegmentLength;
  [WmiDataId(4), read, write, Description("Maximum SCSI data
    payload in bytes in an Data-In or a solicited Data-Out
    iSCSI sequence.") : amended]
    uint32  MaxBurstLength;
  [WmiDataId(5), read, write, Description("maximum amount in
    bytes of unsolicited data an iSCSI initiator may send to
    the target, during the execution of a single SCSI
    command. This covers the immediate data (if any) and the
    sequence of unsolicited Data-Out PDUs (if any) that
    follow the command.") : amended]
    uint32  FirstBurstLength;
  [WmiDataId(6), read, write, Description("Initiator and
    target negotiate the maximum number of outstanding R2Ts
    per task, excluding any implied initial R2T that might
    be part of that task.  An R2T is considered outstanding
    until the last data PDU (with the F bit set to 1) is
    transferred, or a sequence reception timeout (section
    6.12.1) is encountered for that data sequence.") :
    amended]
    uint32  MaxOutstandingR2T;
};
```

When the WMI tool suite compiles the preceding class definition, it produces the [**MSiSCSI\_HBASessionConfig**](https://msdn.microsoft.com/library/windows/hardware/ff563021) data structure.

 

 





