import { GlobalStateProvider } from './context/GlobalStateContext'
import './App.css'
import { Outlet } from 'react-router-dom'

function App() {

  return (
    <>
    <GlobalStateProvider>
      <Outlet />
    </GlobalStateProvider>
    </>
  )
}

export default App;
