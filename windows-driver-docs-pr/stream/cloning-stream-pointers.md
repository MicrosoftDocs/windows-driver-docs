---
title: Cloning Stream Pointers
description: Cloning Stream Pointers
keywords:
- stream pointers WDK AVStream , cloning
- cloning stream pointers WDK AVStream
- duplicating stream pointers WDK AVStream
- copying stream pointers WDK AVStream
ms.date: 04/20/2017
---

# Cloning Stream Pointers





Multiple stream pointers can reference a single frame. To duplicate a stream pointer, call [**KsStreamPointerClone**](/windows-hardware/drivers/ddi/ks/nf-ks-ksstreampointerclone).

The resulting copy of the stream pointer is referred to as a stream pointer *clone*. The clone is a new stream pointer that is identical to the parent. Initially, the clone references the same frame and has the same lock status. After it is created, a clone is independent of its parent stream pointer.

You can clone leading edge, trailing edge, or current clone stream pointers.

Adding a clone stream pointer increments the reference count on that particular frame. See [Introduction to Stream Pointers](introduction-to-stream-pointers.md) For more information about reference counts.

Enumerate clone stream pointers by using [**KsPinGetFirstCloneStreamPointer**](/windows-hardware/drivers/ddi/ks/nf-ks-kspingetfirstclonestreampointer) and [**KsStreamPointerGetNextClone**](/windows-hardware/drivers/ddi/ks/nf-ks-ksstreampointergetnextclone).

Clones exist until you delete them by calling [**KsStreamPointerDelete**](/windows-hardware/drivers/ddi/ks/nf-ks-ksstreampointerdelete). When the minidriver deletes a clone, AVStream decrements the reference count for the corresponding frame.

See [AVStream DMA Services](avstream-dma-services.md) for an example of how to use stream pointer clones.

 

