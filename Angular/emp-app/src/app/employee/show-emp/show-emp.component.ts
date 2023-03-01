import { Component, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-show-emp',
  templateUrl: './show-emp.component.html',
  styleUrls: ['./show-emp.component.css']
})
export class ShowEmpComponent implements OnInit{

  constructor(private service:SharedService, private route: Router) {}

  EmployeeList:any=[];

  ActivateEditEmpComp:boolean=false;
  emp:any;

  ngOnInit(): void {
    this.refreshEmpList();
  }

  editClick(item:any){
    this.emp=item;
    this.ActivateEditEmpComp=true;
  }

  deleteClick(item:any){
    if(confirm("Are you sure..??"))
     this.service.deleteEmpList(item.id).subscribe(data=>{
      alert(data.toString());
      this.refreshEmpList();
     })
  }

  closeClick(){
    this.ActivateEditEmpComp=false;
    this.refreshEmpList();
  }

  refreshEmpList(){
    this.service.getEmpList().subscribe(data=>{
      this.EmployeeList=data;
    });
  }

  logoutUser(){
    this.service.removeToken();
    this.route.navigate(['']);
  }

}
