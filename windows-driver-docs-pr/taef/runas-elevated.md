---
title: RunAs Elevated
description: TAEF ensures that the test is run in an elevated process by spawning an elevated process to run the test if necessary.
ms.assetid: 6292E431-6EB5-4962-BBB0-B86FC4CE4643
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# RunAs Elevated


TAEF ensures that the test is run in an elevated process by spawning an elevated process to run the test if necessary.

**Note: The user executing TAEF must be a member of the administrators group in order to execute tests marked with RunAs=Elevated.** This is due to the fact that non-admins do not have a split token to elevate. If a non-admin attempts to run a test which is marked with RunAs=Elevated, **the test will be marked as blocked**.

**Note**  On computers running versions of Windows older than Windows Vista, you must run elevated tests from an administrator process.

 

## <span id="Specifying_RunAs_on_the_Command_Line_"></span><span id="specifying_runas_on_the_command_line_"></span><span id="SPECIFYING_RUNAS_ON_THE_COMMAND_LINE_"></span>Specifying RunAs on the Command Line


``` syntax
te unittests\* /runas:elevated
```

## <span id="Marking_Tests_with_RunAs_"></span><span id="marking_tests_with_runas_"></span><span id="MARKING_TESTS_WITH_RUNAS_"></span>Marking Tests with RunAs


Test metadata can be used to specify the runas type of an assembly, class or test method.

**Note**  RunAs values specified in metadata override RunAs values specified on the command line. For example, a test marked with **runas:system** test metadata will still be run as Local System even if **/runas:elevated** is specified on the command line.

 

Example (native code)

```ManagedCPlusPlus
class MyTests
{
    TEST_CLASS(MyTests);

    BEGIN_TEST_METHOD(ElevatedTest)
        TEST_METHOD_PROPERTY(L"RunAs", L"Elevated")
    END_TEST_METHOD()
};
```

## <span id="related_topics"></span>Related topics


[RunAs](runas.md)

 

 






