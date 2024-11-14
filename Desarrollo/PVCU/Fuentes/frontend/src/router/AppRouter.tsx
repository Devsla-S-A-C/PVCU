import { createBrowserRouter } from "react-router-dom";

// Epicas
import { LoginPage, RegisterPage } from "../pages/Epica01";
import { ProfileBuyerPage } from "../pages/Epica02";
import { MainPage, SearchPage, SearchSellers } from "../pages/Epica03";
import {
  PlansPage,
  PayPlanPage,
  PaymentConfirmation,
  RegisterTrademark,
  loader as plansLoader,
} from "../pages/Epica05";
import {
  ProductsManagementPage,
  MyPublishedProductsPage,
  PublishProductPage,
  EditProductPage,
  ShoppingCartPage,
  FavouritesPage,
  ProductPage,
} from "../pages/Epica04";
import { Layout } from "../components/layouts/Layout";
import { PrivateRoute } from "../components/Epica1/PrivateRoute";
import {
  PendingPurchasesPage,
  PurchaseHistoryPage,
  PurchaseManagementPage,
} from "@/pages/Epica06";
import { Chat } from "@/pages/Epica06/Chat";
import { ContactPage } from "../pages/Epica08/ContactPage";

const routes = createBrowserRouter([
  {
    path: "/login",
    element: <LoginPage />,
    // loader:
  },
  {
    path: "/register",
    element: <RegisterPage />,
  },
  {
    element: <Layout />,
    // loader:
    children: [
      {
        path: "/",
        element: <MainPage />,
        // loader:
      },
      {
        path: "/search",
        element: <SearchPage />,
        // loader:
      },
      {
        path:"/sellers",
        element:<SearchSellers />
      },
      { 
        path:"/contact",
        element:<ContactPage />
      },
      {
        path: "/profile-buyer",
        element: (
          <PrivateRoute>
            <ProfileBuyerPage />
          </PrivateRoute>
        ),
        // loader:
      },
      {
        // path: "/product/productId",
        path: "/product",
        element: <ProductPage />,
        // loader:
      },
      {
        path: "/products-management",
        element: (
          <PrivateRoute>
            <ProductsManagementPage />
          </PrivateRoute>
        ),
        // loader:
      },
      {
        path: "/my-published-products",
        element: (
          <PrivateRoute>
            <MyPublishedProductsPage />
          </PrivateRoute>
        ),
        // loader:
      },
      {
        path: "/publish-product",
        element: (
          <PrivateRoute>
            <PublishProductPage />
          </PrivateRoute>
        ),
        // loader:
      },
      {
        // path: "/:userId/edit-product/productId",
        path: "/edit-product/:productId",
        element: (
          <PrivateRoute>
            <EditProductPage />
          </PrivateRoute>
        ),
      },
      {
        path: "/favourites",
        element: (
          <PrivateRoute>
            <FavouritesPage />
          </PrivateRoute>
        ),
        // loader:
      },
      {
        path: "/shopping-cart",
        element: (
          <PrivateRoute>
            <ShoppingCartPage />
          </PrivateRoute>
        ),
        // loader:
      },
      {
        path: "/plans",
        element: (
          <PrivateRoute>
            <PlansPage />
          </PrivateRoute>
        ),
        loader: plansLoader,
      },
      {
        path: "/pay-plan",
        element: (
          <PrivateRoute>
            <PayPlanPage />
          </PrivateRoute>
        ),
      },
      {
        path: "/register-trademark",
        element: (
          <PrivateRoute>
            <RegisterTrademark />
          </PrivateRoute>
        ),
      },
      {
        path: "/payment-confirmation",
        element: (
          <PrivateRoute>
            <PaymentConfirmation />
          </PrivateRoute>
        ),
      },
      {
        path: "/purchase-management",
        element: <PurchaseManagementPage />,
        children: [
          {
            path: "purchase-history",
            element: <PurchaseHistoryPage />,
          },
          {
            path: "pending-purchase",
            element: <PendingPurchasesPage />,
          },
        ],
      },
      {
        path: "/chat",
        element: <Chat></Chat>,
      },
    ],
  },
]);

export default routes;
