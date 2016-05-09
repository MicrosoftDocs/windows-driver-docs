---
title: The Changer Driver Model
description: The Changer Driver Model
ms.assetid: 87a70ecf-e518-4c22-945b-9056b59fed5a
keywords: ["changer drivers WDK storage , architecture", "storage changer drivers WDK , architecture", "transport element WDK changer", "data transfer elements WDK changer", "storage elements WDK changer", "IEport WDK changer", "import/export element WDK changer", "doors WDK changer", "removable storage manager WDK changer", "RSM WDK changer"]
---

# The Changer Driver Model


## <span id="ddk_the_changer_driver_model_kg"></span><span id="DDK_THE_CHANGER_DRIVER_MODEL_KG"></span>


The following figure shows the relationship between a changer driver, user-mode applications and services, mass storage and port drivers, and a changer device.

![diagram illustrating relationships between a changer driver, user-mode applications and services, mass storage and port drivers, and a changer device](images/changer.png)

Changer Driver Model

As shown in this figure, transfers of user data are handled by the appropriate mass storage driver for changer's drives, using the same Microsoft Win32 requests as for a stand-alone drive. However, a mass storage driver must handle the [**IOCTL\_STORAGE\_GET\_MEDIA\_TYPES\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff560563) I/O request in order to control changer's drives.

User-mode applications access changer's elements through a user-mode service called the removable storage manager (RSM). RSM is the only client of a changer driver and it reserves the changer for exclusive use. RSM sends requests involving changer's elements (for example, to mount a piece of media in a drive) to the changer driver. User-mode applications cannot send requests directly to the changer driver. For details on RSM, see the Microsoft Windows SDK documentation.

The elements of a changer include:

-   *Transport element*

    The robotic component that moves media between other elements in the changer. Most changers have a single transport element with either one or two pickers that hold the media being moved. A high-end, fault-tolerant changer might have more than one transport element.

-   *Data transfer elements*

    The drives from which the data is read and written to media. For example, magnetic or optical disk, tape, CD-ROM, or DVD. Typically, a changer contains only one kind of drive.

-   *Storage elements*

    The slots in which media are stored when not mounted in drives.

A changer might also have either one or both of the following elements:

-   *Import/export*(IEport)

    An element where an operator can insert or remove one or more, but not all, media in the changer.

-   *Door*

    Provides access to all media in the changer at one time. A changer's door can be a physical door that an operator opens, or a single magazine that holds all media.

A changer miniclass driver reports the type and number of a changer's elements in a [**GET\_CHANGER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff554979) structure when requested by the changer class driver. In particular, the miniclass driver must report IEports and doors according to these definitions, regardless of the elements' physical appearance, so that an application can issue appropriate requests to those elements.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20The%20Changer%20Driver%20Model%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




