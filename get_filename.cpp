#include <afxwin.h>
#include <windows.h>
#include <ShlObj.h>
#define PATH_LEN 512
bool get_path(TCHAR *szBuffer){
	BROWSEINFO BrInfo;
	CWnd *cw=new CWnd();
	::ZeroMemory(&BrInfo,sizeof(BROWSEINFO));
	::ZeroMemory(szBuffer, 512); 

	BrInfo.hwndOwner = cw->GetSafeHwnd(); 
	BrInfo.lpszTitle = _T("Select Folder");
	BrInfo.ulFlags = BIF_NEWDIALOGSTYLE | BIF_EDITBOX | BIF_RETURNONLYFSDIRS;
	LPITEMIDLIST pItemIdList = ::SHBrowseForFolder(&BrInfo);
	::SHGetPathFromIDList(pItemIdList, szBuffer);				// 파일경로 읽어오기

	CString str;
	str.Format(_T("%s"),szBuffer);
	if(str.GetLength()!=0)
		AfxMessageBox(str);
	else
		AfxMessageBox(_T("You haven't selected a path"));
	return true;
}
int main(void){
	TCHAR path[PATH_LEN];
    get_path(path);
    return 0;
}