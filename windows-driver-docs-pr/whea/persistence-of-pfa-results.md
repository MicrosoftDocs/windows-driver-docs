---
title: Persistence of PFA Results
author: windows-driver-content
description: Persistence of PFA Results
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: de79b87e-2c9a-4181-b531-8ad283bb9d5b
---

# Persistence of PFA Results


Whenever Predictive Failure Analysis (PFA) predicts that an Error Correction Code (ECC) memory page is likely to fail based on the current PFA registry settings, PFA stores (or *persists*) the page frame number (PFN) for the memory page. PFA persists the PFN in a list within the **{badmemory}** object of the Boot Configuration Data (BCD) system store. This list contains the PFNs for all memory pages that the PFA has predicted are likely to fail. Whenever the Windows operating system is started, it excludes the memory pages in this list from being used by the system.

**Note**  There is no industry standard for mapping a physical memory PFN to a specific physical memory module. Thus, WHEA cannot provide information about which memory modules are failing.

 

Windows does not provide an automated mechanism for clearing this list from the BCD system store. When the failing system memory is replaced, a system administrator must clear this list manually by using the BCDEdit command-line tool. If the list is not cleared, Windows will continue to exclude the memory pages in the list from being used by the system, even if the failing memory modules have been replaced. For more information about managing the PFA memory list by using the BCDEdit tool, see [How to Manage the PFA Memory List](how-to-manage-the-pfa-memory-list.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20Persistence%20of%20PFA%20Results%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


