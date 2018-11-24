---
title: Parallel
description: Parallel
ms.assetid: E2AF7B3A-B614-4fe1-9CFB-0860F68E895C
ms.date: 04/20/2017
ms.localizationpriority: medium
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

```cpp
class MyTests
{

    TEST_CLASS(MyTests);

    BEGIN_TEST_METHOD(ParallelTest)
        TEST_METHOD_PROPERTY(L"Parallel", L"true")
    END_TEST_METHOD()
};
```

As with other general metadata in TAEF, this can be specified at the class or module level & will be inherited by all tests contained within that class or module. For example, to mark an entire assembly as parallelizable you could do the following (outside any class or test specification) in a cpp file compiled into your test DLL:

```cpp
BEGIN_MODULE()
    MODULE_PROPERTY(L"Parallel", L"true");
END_MODULE()
```

This wider-scope can then be overriden at smaller scopes to disable parallelism for particular test cases or classes as follows:

```cpp
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

 

 





