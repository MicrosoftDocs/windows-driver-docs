---
title: Semantic Model Checks
description: Semantic Model Checks
ms.assetid: 7e050067-1f90-4088-a1d9-63d03af81b2d
keywords:
- semantic model checks WDK file systems
- semantic model checks WDK file systems , about semantic model checks
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




