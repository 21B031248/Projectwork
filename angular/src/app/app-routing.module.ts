import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WinesComponent } from './compoments/wines/wines.component';
import { CartComponent } from './compoments/cart/cart.component';
import { CheckoutComponent } from './compoments/checkout/checkout.component';

const routes: Routes = [
  {
    path: '',
    component: WinesComponent,
  },
  {
    path: 'cart',
    component: CartComponent,
  },
  {
    path: 'checkout',
    component: CheckoutComponent,
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
