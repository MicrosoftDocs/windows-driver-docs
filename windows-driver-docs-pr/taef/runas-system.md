---
title: RunAs System
description: TAEF runs the test as Local System.
ms.date: 04/20/2017
---

# RunAs System

TAEF runs the test as Local System.

> [!NOTE]
> The tests that you run as Local System should not create any user interfaces (UI). If your tests need to create or interact with UI, you need to move your UI-related code into separate executables that are launched on a desktop from your tests using [**CreateProcessAsUser function**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessasusera).

## <span id="Specifying_RunAs_on_the_Command_Line_"></span><span id="specifying_runas_on_the_command_line_"></span><span id="SPECIFYING_RUNAS_ON_THE_COMMAND_LINE_"></span>Specifying RunAs on the Command Line

``` syntax
te unittests\* /runas:system
```

## <span id="Marking_Tests_with_RunAs_"></span><span id="marking_tests_with_runas_"></span><span id="MARKING_TESTS_WITH_RUNAS_"></span>Marking Tests with RunAs

Test metadata can be used to specify the runas type of an assembly, class or test method.

> [!NOTE]
> RunAs values specified in metadata override RunAs values specified on the command line. For example, a test marked with **runas:system** test metadata will still be run as Local System even if **/runas:elevated** is specified on the command line.

Example (native code)

```ManagedCPlusPlus
class MyTests
{
    TEST_CLASS(MyTests);

    BEGIN_TEST_METHOD(SystemTest)
        TEST_METHOD_PROPERTY(L"RunAs", L"System")
    END_TEST_METHOD()
};
```

## <span id="related_topics"></span>Related topics

[RunAs](runas.md)
