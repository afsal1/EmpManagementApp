import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class SharedService {
  readonly APIUrl = "http://127.0.0.1:8000/api/v1/user";

  constructor(private http:HttpClient) { }

  onLogin(obj:any){
    return this.http.post(this.APIUrl + '/user_login_view/', obj);
  }

  onSignup(obj:any){
    return this.http.post(this.APIUrl + '/user_register_view/', obj);
  }

  removeToken(){
    localStorage.removeItem('access_token');
  }

  onHomeView():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/user_home_view/');
  }

  getEmpList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/employee/');
  }

  updateEmpList(val:any){
    return this.http.patch(this.APIUrl + '/update_delete_employee/'+ val.id + '/', val);
  }

  deleteEmpList(val:any){
    return this.http.delete(this.APIUrl + '/update_delete_employee/'+ val +'/');
  }
}
