---
title: Custom UI Design Information
description: Custom UI Design Information
ms.assetid: ec1da6d4-a357-4e23-a476-885fbf6441b7
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Custom UI Design Information


If you design your own sAPOs to replace the system-supplied sAPOs, you must provide a custom user interface for configuring the system effects features of your sAPO.

In this case, the user interface will not be a replacement for the system-supplied **Enhancements** property page. And adding a new property page to the **Sound** applet in the Control Panel, involves adding a new tab to the system-supplied **Sound** applet. This means that when the custom sAPOs are registered and initialized, their property page will be available along with the system-supplied **Enhancements** page. It is difficult and complicated to implement communication across the property pages of two different sAPOs. So it is possible that some default settings on the **Enhancements** page will conflict with feature settings on the new property page.

Therefore the most practical approach here is to implement a separate UI for configuring the custom sAPOs that you developed to replace the system-supplied sAPOs. To develop and implement your custom UI, perform the following steps.

1.  [Develop a custom UI](https://go.microsoft.com/fwlink/p/?linkid=106006) for configuring your system effects features

2.  [Create a DLL](https://go.microsoft.com/fwlink/p/?linkid=106014) package from your custom UI

3.  Create or modify an [INF file](https://msdn.microsoft.com/library/windows/hardware/ff549520) for installing and registering your DLL

 

 




