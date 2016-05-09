---
title: Semantic Model Checks
description: Semantic Model Checks
ms.assetid: 7e050067-1f90-4088-a1d9-63d03af81b2d
keywords: ["semantic model checks WDK file systems", "semantic model checks WDK file systems , about semantic model checks"]
---

# Semantic Model Checks


## <span id="ddk_semantic_model_checks_if"></span><span id="DDK_SEMANTIC_MODEL_CHECKS_IF"></span>


In discussing file systems and security, we distinguish between those checks that the file system makes that are part of its semantic model, such as shared file access or special file attributes, and those checks that the file system makes that are part of the security information of the file. This section focuses on checks needed to comply with the semantic model. A later section discusses specific steps needed by a file system to perform security checks that are specific to the security information policies of the file system.

This section includes the following topics:

[Create Processing](create-processing.md)

[Delete on Close](delete-on-close.md)

[Executable Images](executable-images.md)

[Rename and Hard Link Processing](rename-and-hard-link-processing.md)

[Set File Information Processing](set-file-information-processing.md)

[Neither I/O Operations](neither-i-o-operations.md)

[File System Control Processing](file-system-control-processing.md)

[Media Validation](media-validation.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Semantic%20Model%20Checks%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




