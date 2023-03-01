import { Component } from '@angular/core';
import { SharedService } from '../shared.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.css']
})
export class HomePageComponent {
  constructor (private service:SharedService, private route: Router) {}

  UserList:any=[];

  ngOnInit(): void {
    this.getUser();
  }

  getUser(){
    this.service.onHomeView().subscribe(data=>{
      this.UserList=data;
      console.log(this.UserList)
    });
  }

  logoutUser(){
    this.service.removeToken();
    this.route.navigate(['']);
  }

}
