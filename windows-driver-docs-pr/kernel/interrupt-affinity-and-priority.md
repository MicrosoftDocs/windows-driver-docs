---
title: Interrupt Affinity
description: Interrupt Affinity
keywords: ["interrupt service routines WDK kernel , affinity", "ISRs WDK kernel , affinity", "affinity policy WDK interrupts", "IRQ_DEVICE_POLICY", "processor affinity WDK kernel"]
ms.date: 06/16/2017
---

# Interrupt Affinity


The *affinity* of an interrupt is the set of processors that can service the interrupt. Each device has an *affinity policy*. The operating system uses the affinity policy to compute the affinity for that device's interrupts. The affinity policy can be specified in the device's INF file or registry settings.

Starting with Windows Vista, administrators can use the registry to set an affinity policy for an interrupt.

Administrators can set the following entries under the **\\Interrupt Management\\Affinity Policy** registry key:

-   **DevicePolicy** is a REG\_DWORD value that specifies an affinity policy. For possible values and their meanings, see [**IRQ\_DEVICE\_POLICY**](/windows-hardware/drivers/ddi/wdm/ne-wdm-_irq_device_policy). Microsoft recommends using the default policy if applicable.


-   **AssignmentSetOverride** can be a REG_BINARY, REG_DWORD, or REG_QWORD value that specifies a [**KAFFINITY**](#about-kaffinity) mask. For REG_BINARY, size must be less than or equal to the KAFFINITY size for the platform, and input byte order is little endian. If **DevicePolicy** is 0x04 (**IrqPolicySpecifiedProcessors**), then this mask specifies a set of processors to assign the device's interrupts to.

A driver's INF file can provide default settings for the registry values. Here is an example of how to set the **DevicePolicy** value to **IrqPolicyOneCloseProcessor** in the INF file. For more information, see [**INF AddReg Directive**](../install/inf-addreg-directive.md).

```cpp
[install-section-name.HW]
AddReg=add-registry-section 

[add-registry-section]
HKR, "Interrupt Management\Affinity Policy", DevicePolicy, 0x00010001, 2
```

The system makes the registry settings available to the device's driver when it sends the [**IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS**](./irp-mn-filter-resource-requirements.md) IRP to the driver. The operating system provides an [**IO\_RESOURCE\_DESCRIPTOR**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_resource_descriptor) structure for each interrupt with the **Type** member set to **CmResourceTypeInterrupt**. For a message-signaled interrupt, the CM\_RESOURCE\_INTERRUPT\_MESSAGE bit of the **Flags** member is set; otherwise, it is clear. The **u.Interrupt** member describes the settings for the interrupt.

The following table gives the correspondence between registry settings and members of **u.Interrupt**.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Registry Value</th>
<th>Member of u.Interrupt</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>DevicePolicy</strong></p></td>
<td><p><strong>AffinityPolicy</strong></p></td>
</tr>
<tr class="even">
<td><p><strong>AssignmentSetOverride</strong></p></td>
<td><p><strong>TargetedProcessors</strong></p></td>
</tr>
</tbody>
</table>

## About KAFFINITY

The KAFFINITY type is an affinity mask that represents a set of logical processors in a group.

```cpp
typedef ULONG_PTR  KAFFINITY;
```

The KAFFINITY type is 32 bits on a 32-bit version of Windows and is 64 bits on a 64-bit version of Windows.

If a group contains n logical processors, the processors are numbered from 0 to n-1. Processor number i in the group is represented by bit i in the affinity mask, where i is in the range 0 to n-1. Affinity mask bits that do not correspond to logical processors are always zero.

For example, if a KAFFINITY value identifies the active processors in a group, the mask bit for a processor is one if the processor is active, and is zero if the processor is not active.

The number of bits in the affinity mask determines the maximum number of logical processors in a group. For a 64-bit version of Windows, the maximum number of processors per group is 64. For a 32-bit version of Windows, the maximum number of processors per group is 32. Call the [**KeQueryMaximumProcessorCountEx**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-kequerymaximumprocessorcountex) routine to obtain the maximum number of processors per group. This number depends on the hardware configuration of the multiprocessor system, but can never exceed the fixed 64-processor and 32-processor limits that are set by the 64-bit and 32-bit versions of Windows, respectively.

The [**GROUP_AFFINITY**](/windows-hardware/drivers/ddi/miniport/ns-miniport-_group_affinity) structure contains an affinity mask and a group number. The group number identifies the group to which the affinity mask applies.

Kernel routines that use the KAFFINITY type include [**IoConnectInterrupt**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioconnectinterrupt), [**KeQueryActiveProcessorCount**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-kequeryactiveprocessorcount), and [**KeQueryActiveProcessors**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-kequeryactiveprocessors). 

 

 

