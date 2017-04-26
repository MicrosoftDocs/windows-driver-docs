---
title: Authoring Tests
description: Authoring Tests
ms.assetid: 728821AC-9C90-4dae-8A42-2C8E712174DF
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Authoring Tests


TAEF supports running tests that have been written in a variety of development languages. Currently, it supports tests written in native C++, managed code, and scripting languages. In each scenario, the tests are marked-up using language-specific constructs. Code within TAEF interprets the final test files and describes them to the TAEF engine in an intermediate representation. TAEF then manipulates this intermediate representation without having concrete details of how the tests were written.

The following topics provide more information about authoring tests in TAEF:

-   [Authoring Tests in C++](authoring-tests-in-c--.md)
-   [Authoring Tests in C#](authoring-tests-in-c-.md)
-   [Authoring Tests in Scripting Languages](authoring-tests-in-scripting-languages.md)
-   [Authoring Tests in AXE](authoring-tests-in-axe.md)
-   [Verify Framework](verify.md)
-   [Making the Most of TAEF](making-the-most-of-taef.md)
-   [Standard Test Metadata](standard-test-metadata.md)
-   [Conditional Metadata](conditional-metadata.md)
-   [Reboot](reboot.md)
-   [Runtime Parameters](runtime-parameters.md)
-   [Threading Models](threading-models.md)
-   [Execution Groups](execution-groups.md)
-   [Assembly Config Files](assembly-config-files.md)
-   [Device Support](device-support.md)
-   [WexLogger](wexlogger.md)
-   [DeploymentItem Metadata](deploymentitem-metadata.md)

[Authoring Tests in C++](authoring-tests-in-c--.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[taef\taef]:%20Authoring%20Tests%20%20RELEASE:%20%289/12/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




