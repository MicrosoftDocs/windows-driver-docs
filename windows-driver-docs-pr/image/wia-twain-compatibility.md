---
title: WIA-TWAIN Compatibility
description: WIA-TWAIN Compatibility
ms.assetid: f4fe85cc-a201-4cf7-a0f9-74d7514f1447
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA-TWAIN Compatibility





If a device can have two or more drivers, test these drivers thoroughly for compatibility with each other. For example, if one driver leaves the device in an unusable state (such as the driver not sending the close session message in some protocol), the other driver might fail when it tries to communicate with the device. This situation happens often with serial devices.

### WIA and TWAIN in the Same DLL

If you are running a WIA driver and a TWAIN driver at the same time from a single DLL, the WIA service and the TWAIN application will both load an instance of this DLL. The WIA instance of the DLL will build the WIA item tree. This tree represents the folders and images on your camera. Any application that uses WIA (such as My Computer or Scanner and Camera Wizard) will have a copy of the item tree in your driver.

When an image is deleted or added by means of the TWAIN driver, the WIA driver is not notified of this change. As a result, the WIA item tree either will contain images that have been deleted, or will not contain images that have been added. In either case, the driver must refresh its item tree. To do so, the TWAIN driver must order your WIA driver to refresh its item tree when an image has been added or deleted.

One way of doing this is to call **CoCreateInstance**(CLSID\_**IWiaDevMgr**,...) from your TWAIN driver, enumerate all the devices, and search for your device. One way to identify your driver through this enumeration is to create a custom property in your WIA driver so that if the TWAIN driver queries for this property and it exists, you will know that it is your WIA driver. After you have the **IWiaItem** for your driver, send a command to your driver to rebuild its tree (for example, send it a [WIA CMD\_SYNCHRONIZE](wia-driver-command-support.md) command in a call to the **IWiaItem::DeviceCommand** method). **CoCreateInstance**, **IWiaDevMgr**, and **IWiaItem** are described in the Microsoft Windows SDK documentation.

Another way of refreshing the WIA item tree is to create a named [event](wia-driver-event-support.md) in the WIA driver. A thread in your WIA driver can then wait for this event to be signaled. Whenever you delete or add an image by means of the TWAIN driver, the TWAIN driver signals (by calling **SetEvent** (described in the Windows SDK documentation)) on this named event. The thread in your WIA driver will then be released, and the WIA driver will rebuild the tree.

Either way, you should rebuild your tree so that it reflects any changes made to the actual images on the camera or scanner. Make sure that whenever you update the tree by adding or deleting an item from the item tree, that you queue an event (for example, WIA\_EVENT\_ITEM\_DELETED or WIA\_EVENT\_TREE\_UPDATED (for a description of these and other WIA event identifiers, see the Windows SDK documentation)). If you successfully send an event when your tree changes, this will solve the problem with My Computer and other WIA applications not being updated automatically.

**Note**   While your TWAIN and WIA drivers may exist in the same DLL, WIA and TWAIN drivers cannot share the same UI. Each driver must have its own UI.

 

 

 




