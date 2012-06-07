# To change this template, choose Tools | Templates
# and open the template in the editor.
#from Webdriver.testPreProcess import createTestUser
#
##gb_testUserId = testUserIdValue
##gb_testUserGroupId = testUserGroupIdValue
##########################################################
#createTestUser.py
userFirstName = "ztestUser"
userLastName = "ztestUser"
userEmailAdd = "ztestUser@test.com"
userName = "ztestUser"
userPassword = "test"
userPasswordRepeat = "test"
userGroupName = "ztestUserGroup"

searchUserFirstName = u"zab"
searchUserLastName = u"zcd"
searchUserEmailAdd = u"zabcd@abcd.com"
searchUserName = u"zabcd"

editUserFirstName = u"zeditUser"
editUserLastName = u"zeditUser"
editUserEmailAdd = u"zeditUser@test.com"
editUserName = u"zeditUser"

duplicateUserGroup = u"zduplicateUserGroup"
editUserGroup = u"zeditUserGroup"
#*****************************************************************
#createStuffs.py
ModifyMediaGroup = u"ModifyMediaGroup"
TestMediaGroup =u"TestMediaGroup"
#*****************************************************************
#store Hierarchy:
companyTest = u"companyTest"
storeGroupTest = u"storeGroupTest"
storeTest = u"storeTest"
dStore = u"dStore"
assignStore = u"assignStore"
#******************************************************************
classifyProductsCategory = u"test"
classifyProductsKeyword = u"keywordOptions"
classfiyProductsSubCategory = u"subCategoryOptions"

#********************************************************************
testProduct1 = u"atestProduct1"
testProduct2 = u"atestProduct2"
testAcc1 = u"atestzAcc1"
testAcc2 = u"atestzAcc2"

#*****************************************************
duplicateTmp = u"zDuplicateTmp"
editTmpSchedule = u"zeditTmpSchedule"
modifyTmp = u"zmodifyTmp"

#******************************************************
assignLoops = u"zassignLoops"
editLoopSchedule = u"zeditLoopSchedule"
editNameOfLoop = u"editNameOfLoop"

#########################################################
#Update the data here:
#data from createTestUser.py
#Step 1: run createTestUser.py, record the following data; assgin userName to userGroupName;
testUserIdValue = "205"
testUserGroupIdValue = "206"

#Step 2: Run assignPermissions.py

#Step 3: Run createStoreHierarchy.py, record the following data, assign userGroupName to storeTest;
#data from createStuffs.py
companyTestIdValue= "127"
storeGroupTestIdValue = "128"
storeTestIdValue = "129"
dStoreIdValue = "130"
assignStoreIdValue ="131"

#Step 4: Run createMedia.py, record the following data.; Assign MediaEditTest.avi to TestMediaGroup
ModifyMediaGroupIdValue= "402"
TestMediaGroupIdValue = "403"
uploadMediaMediumID = "69"

#Step5:Run createCSCKeyWords.py, record the following data:
classifyProductsCategoryId = "409"
classifyProductsKeywordId = "410"
classfiyProductsSubCategoryId = "411"

#Step 6: Run createProducts.py, record the following data:
testProduct1IdValue="422"
testProduct1IdValue="423"
testAcc1IdValue="424"
testAcc2IdValue="425"

#Step 7: Run createUsersAndGroups, record the following data:
editUserIdValue="221"
duplicateUserGroupIdValue=""
editUserGroupIdValue=""

#Step 8: Run createTemplates,py record the following data:
editTmpScheduleValue="391"
duplicateTmpIdValue="434"
modifyTmpIdValue="434"

#Step 9: Run createLoops.py record the following data:
assignLoopsId="aLCol_attractLoop385"
assignLoopsIdValue="440"
editLoopScheduleId="aLCol_attractLoop440"
editLoopScheduleIdValue="441"
editNameOfLoopId="aLCol_attractLoop441"
editNameOfLoopIdValue="442"



