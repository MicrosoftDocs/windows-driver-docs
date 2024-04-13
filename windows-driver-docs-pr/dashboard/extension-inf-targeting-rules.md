---
title: Extension INF targeting evaluation rules defined
description: Policy defines how extension INFs can be targetted
ms.topic: article
ms.date: 09/22/2020
---

# Extension INF targeting evaluation rules defined

As we move towards properly componentized modern drivers, we’ll share some plans about how we will evaluate these drivers moving forward. 

Please keep in mind the founding principles behind driver componentization: 

>- Base drivers are meant to provide core device functionality and can be broadly targeted.
> 
>- Extension drivers are generally meant to provide system specific customizations and must be specifically targeted.  As a best practice, the INF should only include targeting to a single OEM. For our policy checking and validation, we focus on the HWIDs you choose to publish. The targeting should only include HWIDs and CHIDs which are specifically being customized by the extension INF and limited to a single OEM. 
> 
>- The use of CHID while publishing to every HWID listed will not constitute specific targeting if multiple OEM's HWIDs are referenced in the INF. This practice will fail our policy checks. 

Here is how we’ll evaluate these principles when processing your submissions in Driver Shiproom:

  **Is the Extension INF targeting a 2-ID with no CHID?**
  
  IF YES: Reject. Extension INFs cannot be broadly targeted.

  **Is the Extension INF targeted to systems spanning more than one OEM? (per CHID and HWID analysis)**
  
  IF YES: Reject. Extension INFs cannot span multiple OEM’s systems, as they should be specifically targeted to OEM systems.

  **Is the Extension INF missing a declarative base?**
  
  IF YES: Reject. Extension INFs are only compatible with DCH drivers. The only exception to this rule is if the extension INF matches on an inbox driver (e.g. for firmware update scenarios, or HSA scenarios).

  **How can I extend an inbox driver?**

  If you want to extend a driver that comes as part of Windows, add the following keyword to your Business Justification for the shipping label:
  
  `ExtendsInboxDriver = wdma_usb.inf`
  
  Substitute the specific Windows driver in place of `wdma_usb.inf`.

  If you want to extend multiple drivers, separate the hardware IDs for each inbox driver into their own shipping labels. Do not combine hardware IDs for multiple inbox drivers. Do not combine hardware IDs for inbox drivers with hardware IDs for out-of-box drivers.

Please let us know if you have any questions or feedback about these rules.
