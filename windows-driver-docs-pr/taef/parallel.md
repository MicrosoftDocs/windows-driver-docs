---
title: Parallel
description: Parallel
ms.assetid: E2AF7B3A-B614-4fe1-9CFB-0860F68E895C
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Parallel


TAEF provides a mechanism to execute tests in parallel across multiple processors.

## <span id="Parallelism_Guarantees"></span><span id="parallelism_guarantees"></span><span id="PARALLELISM_GUARANTEES"></span>Parallelism Guarantees


-   No two tests not [marked as parallelizable](#markingtestsasparallelizable) will ever be executed concurrently.
-   Parallel tests can be run concurrently with both other parallel and non-parallel tests.
-   All module/class/test setup and cleanup will be run linearly before and after the relevant test in the same process.
-   Module/class setup may be executed in parallel on different processes if the module or class contains at least one parallel test.
-   Parallel execution mode is incompatible with the [**"/inproc"**](executing-tests.md) execution mechanism.

## <span id="MarkingTestsAsParallelizable"></span><span id="markingtestsasparallelizable"></span><span id="MARKINGTESTSASPARALLELIZABLE"></span>Marking Tests as Parallelizable


Example (native code):

```
class MyTests
{

    TEST_CLASS(MyTests);

    BEGIN_TEST_METHOD(ParallelTest)
        TEST_METHOD_PROPERTY(L"Parallel", L"true")
    END_TEST_METHOD()
};
```

As with other general metadata in TAEF, this can be specified at the class or module level & will be inherited by all tests contained within that class or module. For example, to mark an entire assembly as parallelizable you could do the following (outside any class or test specification) in a cpp file compiled into your test DLL:

```
BEGIN_MODULE()
    MODULE_PROPERTY(L"Parallel", L"true");
END_MODULE()
```

This wider-scope can then be overriden at smaller scopes to disable parallelism for particular test cases or classes as follows:

```
class MyTests
{
    TEST_CLASS(MyTests);

    BEGIN_TEST_METHOD(NonParallelTest)
        TEST_METHOD_PROPERTY(L"Parallel", L"false");
    END_TEST_METHOD()
};
```

Whichever setting is closest to the test method (method metadata is the closest, then class, then module) will be used to decide whether to run this test in parallel with other tests.

## <span id="EnablingParallelismAtTheCommandLine"></span><span id="enablingparallelismatthecommandline"></span><span id="ENABLINGPARALLELISMATTHECOMMANDLINE"></span>Enabling Parallelism at the Command Prompt


Parallel execution is an opt-in feature. While tests may be marked up as parallel, TAEF will continue to execute tests linearly unless parallel execution mode is enabled at the command prompt:

``` syntax
te unittests\* /parallel
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[taef\taef]:%20Parallel%20%20RELEASE:%20%289/12/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




