---
title: Test Isolation
description: Test Isolation
ms.assetid: AC2A0060-45B9-45ff-87ED-69842F9A567D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Test Isolation


TAEF supports running tests in an isolated process. It is possible to control when these processes get replaced with the IsolationLevel metadata and command line option. This can be useful for detecting unintended test dependencies or for reducing the impact of a leaking test.

The following list shows the possible values of the IsolationLevel metadata and command line option and their meanings.

<span id="None"></span><span id="none"></span><span id="NONE"></span>None  
TAEF will not isolate any tests.

<span id="Module"></span><span id="module"></span><span id="MODULE"></span>Module  
TAEF will use a separate process host for each test DLL. **This is the default value.**

<span id="Assembly"></span><span id="assembly"></span><span id="ASSEMBLY"></span>Assembly  
Same as Module

<span id="DLL"></span><span id="dll"></span>DLL  
Same as Module

<span id="Class"></span><span id="class"></span><span id="CLASS"></span>Class  
TAEF will use a separate process host for each test class.

<span id="Method"></span><span id="method"></span><span id="METHOD"></span>Method  
TAEF will use a separate process host for each test. If the test is within an execution group, the same process host will be used for the whole execution group.

<span id="Test"></span><span id="test"></span><span id="TEST"></span>Test  
Same as Method

The IsolationLevel metadata value that is used is the metadata specified closest to the test level. If the command line IsolationLevel option is also set, the value that is used is the one that provides the most isolation.

```cpp
BEGIN_MODULE()
    MODULE_PROPERTY(L"IsolationLevel", L"Class")
END_MODULE()

class MyTestClass1
{
    TEST_CLASS(MyTestClass1);

    BEGIN_TEST_METHOD(MyTest1)
        TEST_METHOD_PROPERTY(L"IsolationLevel", L"Method")
    END_TEST_METHOD()

    TEST_METHOD(MyTest2);
    TEST_METHOD(MyTest3);
};

class MyTestClass2
{
    TEST_CLASS(MyTestClass2);

    TEST_METHOD(MyTest1);
    TEST_METHOD(MyTest2);
};
```

In the above example, three different process hosts are used: one for MyTestClass1::MyTest1, one for the other two methods in MyTestClass1, and one for MyTestClass2. If the user were to add /IsolationLevel:Method to the te.exe's command line, five different process hosts would be used: one for each test.

Note that if a module, class, or test is [metadata-expanded](light-weight-data-driven-testing.md) or [data-driven](data-driven-testing.md) and it is to be isolated, each metadata and/or data expansion is isolated. This can be prevented on the test level by making the test a member of an [execution group](execution-groups.md).

```cpp
class MyTestClass3 :
{
    BEGIN_TEST_CLASS(MyTestClass3)
        TEST_CLASS_PROPERTY(L"Data:MyParameter1", L"{1, 2, 3}")
        TEST_CLASS_PROPERTY(L"IsolationLevel", L"Class")
    END_TEST_CLASS()

    BEGIN_TEST_METHOD(MyTest1)
        TEST_METHOD_PROPERTY(L"Data:MyParameter2", L"{1, 2, 3}")
        TEST_METHOD_PROPERTY(L"IsolationLevel", L"Method")
        TEST_METHOD_PROPERTY(L"ExecutionGroup", L"MyExecutionGroup")
    END_TEST_METHOD()

    TEST_METHOD(MyTest2);
    TEST_METHOD(MyTest3);
};
```

In this example, six different process hosts are used. Each of the three values of MyParameter1 is isolated and MyTest1 is isolated from MyTest2 and MyTest3. The three values of MyParameter2 are not isolated since they are in the same execution group.

 

 





