---
title: Storage class memory glossary
description: Glossary page
Robots: noindex, nofollow
ms.assetid: 6897E3E2-9F93-4100-BB99-1B224AFE2B68
---

# Storage class memory glossary


## <span id="starts_with_A"></span><span id="starts_with_a"></span><span id="STARTS_WITH_A"></span>A


<span></span>**Abort**  
An operation that stops the currently running operation on the NVDIMM-N module.

<span></span>**Arm**  
An operation that enables or disables one or more triggers for a save operation on the NVDIMM-N module.

## <span id="starts_with_B"></span><span id="starts_with_b"></span><span id="STARTS_WITH_B"></span>B


<span></span>**Backup**  
The process of saving DRAM contents from the NVDIMM-N module DRAM to the non-volatile memory. Energy-backed devices, like the ones covered in this document, use a discrete Energy Source to provide energy in case a power loss triggers the backup.

<span></span>**BIOS (Basic Input/Output System)**  
The host uses this code to initialize its hardware prior to loading and launching an operating system.

## <span id="starts_with_D"></span><span id="starts_with_d"></span><span id="STARTS_WITH_D"></span>D


<span></span>**Device-Managed Policy**  
An Energy Source policy where the module manages the Energy Source the save operation uses.

## <span id="starts_with_E"></span><span id="starts_with_e"></span><span id="STARTS_WITH_E"></span>E


<span></span>**Energy Source (ES)**  
A device that is capable of storing and providing energy to the NVDIMM-N module during a save operation.

<span></span>**Erase**  
An operation that deletes the previously saved DRAM content in the NVDIMM-N module’s non-volatile memory.

## <span id="starts_with_F"></span><span id="starts_with_f"></span><span id="STARTS_WITH_F"></span>F


<span></span>**Factory Default**  
An operation that erases all non-volatile memory on the NVDIMM-N module and resets readable registers to the factory default values except the data needed to determine warranty compliance. This operation does not impact firmware on the module.

<span></span>**Firmware Operation**  
An operation that is related to updating the firmware on the NVDIMM-N module.

## <span id="starts_with_H"></span><span id="starts_with_h"></span><span id="STARTS_WITH_H"></span>H


<span></span>**Host**  
The system in which the NVDIMM-N module is installed.

<span></span>**Host-Managed Policy**  
An ES policy where the host manages the ES used during the save operation of the NVDIMM-N modules.

## <span id="starts_with_I"></span><span id="starts_with_i"></span><span id="STARTS_WITH_I"></span>I


<span></span>**I²C Bus (Inter-Integrated Circuit)**  
A bidirectional 2-wire bus for efficient inter-integrated circuit control. The current designs of NVDIMM-N modules use the I²C bus.

## <span id="starts_with_N"></span><span id="starts_with_n"></span><span id="STARTS_WITH_N"></span>N


<span></span>**NVDIMM-N**  
The JEDEC-defined term for an NVDIMM that provides persistent DRAM using NAND flash.

## <span id="starts_with_R"></span><span id="starts_with_r"></span><span id="STARTS_WITH_R"></span>R


<span></span>**Restore**  
The process of restoring previously saved DRAM contents from non-volatile memory to the NVDIMM-N module’s DRAM.

## <span id="starts_with_S"></span><span id="starts_with_s"></span><span id="STARTS_WITH_S"></span>S


<span></span>**Save**  
The process of copying the DRAM contents of the NVDIMM-N into non-volatile memory when power is lost. The save operation is initiated when an enabled trigger occurs.

## <span id="starts_with_V"></span><span id="starts_with_v"></span><span id="STARTS_WITH_V"></span>V


<span></span>**Vendor Log Page**  
An optional area on the module that is accessible by the host and contains vendor specific data useful to triage issues on the NVDIMM-N module.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Storage%20class%20memory%20glossary%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




