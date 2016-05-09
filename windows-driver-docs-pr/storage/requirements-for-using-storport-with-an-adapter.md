---
title: Requirements for Using Storport with an Adapter
description: Requirements for Using Storport with an Adapter
ms.assetid: 85adf2f9-e9eb-40d8-9177-adda150a8ea4
---

# Requirements for Using Storport with an Adapter


## <span id="ddk_requirements_for_using_storport_with_an_adapter_kg"></span><span id="DDK_REQUIREMENTS_FOR_USING_STORPORT_WITH_AN_ADAPTER_KG"></span>


In order to improve performance and enhance stability, Storport does not provide support for certain kinds of devices (mostly older devices with limited feature sets). In addition to degrading performance, support for these devices complicates the port driver, slowing down miniport driver development and testing.

The following list details the features that devices, adapters, and miniport drivers must all support, in order to function with Storport:

-   Bus-mastering DMA. Storport does not support either programmed I/O or subordinate-mode DMA.

-   Scatter/gather I/O. Miniport drivers must support at least 16 physical breaks in their scatter/gather list implementation. Miniport drivers that work with Storport should be able to support up to 255 physical breaks in the same manner as SCSI Port miniport drivers.

-   SCSI tagged queuing. The Storport driver will issue up to 254 requests per logical unit. SCSI Port miniport drivers that make use of the fact that SCSI Port never issued more than 254 requests per adapter must be modified to accept a much larger number of requests.

-   SCSI autorequest sense. Disabling is not supported.

-   Support for larger sense buffers. Miniport drivers that work with Storport must not be designed with fixed-size sense buffers in view. Miniport drivers must use the size passed in the SRB.

-   Plug and Play. Because miniport drivers that work with Storport must be enabled for Plug and Play, the port driver takes care of all shared resource acquisition and management.

-   Multi-Tier Resets. Adapters must support tiered resets. For more information, see [Multi-Tier Reset in Storport](multi-tier-reset-in-storport.md).

-   RAID Adapters that expose virtual logical units are required to support SCSI Inquiry Vital Product Data pages 00h, 80h, and 83h. For example, a host-based RAID adapter must respond to a SCSI Inquiry command with Vital Product Data Page set to 01h for the following pages: 0 (supported vital product data pages), 80h (unit serial number page), and 83h (device identification page). These commands can be handled either by the adapter's firmware or synthesized in the miniport driver.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Requirements%20for%20Using%20Storport%20with%20an%20Adapter%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




