---
title: Handling Interrupts
description: Handling Interrupts
ms.assetid: 5C8CB68A-EAE6-4AF9-8B10-F8B73B50DEB2
---

# Handling Interrupts


\[This topic applies to UMDF 1.*x*.\]

Starting in UMDF version 1.11, UMDF drivers can handle hardware interrupts. UMDF supports both line-based (both level-triggered and edge-triggered) and message-signaled (MSI) interrupts.

Line-based, level-triggered interrupts are available starting in Windows 8. MSI and line-based, edge-triggered interrupts are available on all operating systems that UMDF 1.11 supports.

Framework-based drivers manage hardware interrupts by using framework interrupt objects.

## In this section


-   [Creating an Interrupt Object](creating-an-interrupt-object-umdf.md)
-   [Enabling and Disabling Interrupts](enabling-and-disabling-interrupts-umdf.md)
-   [Servicing an Interrupt](servicing-an-interrupt-umdf.md)
-   [Using Work Items](using-workitems.md)
-   [Synchronizing Interrupt Code](synchronizing-interrupt-code-umdf.md)
-   [Deleting an Interrupt Object](deleting-an-interrupt-object.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Handling%20Interrupts%20%20RELEASE:%20%283/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




