---
title: Persistence of PFA Results
description: Persistence of PFA Results
ms.assetid: de79b87e-2c9a-4181-b531-8ad283bb9d5b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Persistence of PFA Results


Whenever Predictive Failure Analysis (PFA) predicts that an Error Correction Code (ECC) memory page is likely to fail based on the current PFA registry settings, PFA stores (or *persists*) the page frame number (PFN) for the memory page. PFA persists the PFN in a list within the **{badmemory}** object of the Boot Configuration Data (BCD) system store. This list contains the PFNs for all memory pages that the PFA has predicted are likely to fail. Whenever the Windows operating system is started, it excludes the memory pages in this list from being used by the system.

**Note**  There is no industry standard for mapping a physical memory PFN to a specific physical memory module. Thus, WHEA cannot provide information about which memory modules are failing.

 

Windows does not provide an automated mechanism for clearing this list from the BCD system store. When the failing system memory is replaced, a system administrator must clear this list manually by using the BCDEdit command-line tool. If the list is not cleared, Windows will continue to exclude the memory pages in the list from being used by the system, even if the failing memory modules have been replaced. For more information about managing the PFA memory list by using the BCDEdit tool, see [How to Manage the PFA Memory List](how-to-manage-the-pfa-memory-list.md).

 

 




