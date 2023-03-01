import { Component, Input } from '@angular/core';
import { SharedService } from 'src/app/shared.service';

@Component({
  selector: 'app-edit-emp',
  templateUrl: './edit-emp.component.html',
  styleUrls: ['./edit-emp.component.css']
})
export class EditEmpComponent {
  constructor (private service:SharedService) {}

  @Input() emp:any;
  id:any;
  first_name:any;
  last_name:any;

  ngOnInit(): void {
    this.id=this.emp.id;
    this.first_name=this.emp.first_name;
    this.last_name=this.emp.last_name;
  }

  updateEmpList(){
    var val = {id:this.id,
    first_name:this.first_name,
    last_name:this.last_name};
    this.service.updateEmpList(val).subscribe(res=>{
      console.log(this.first_name);
    });
  }

}
