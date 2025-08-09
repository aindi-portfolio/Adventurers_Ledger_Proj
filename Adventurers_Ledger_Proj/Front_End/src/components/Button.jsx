export default function Button({ onClick, type = 'button', children }) {
    return (
        <button 
            type={type} 
            onClick={onClick} 
            className={`min-w-20 px-6 py-3 bg-gradient-to-r from-yellow-800 to-yellow-500 text-white
                font-semibold rounded-lg shadow-md hover:from-yellow-600 hover:to-yellow-400
                hover:scale-105 transition-transform duration-200 border-2 border-yellow-800`}
        >
            {children}
        </button>
    );
}

function MysticButton({ onClick, type = 'button', children }) {
    return (
        <button 
            type={type} 
            onClick={onClick} 
            className={`min-w-20 px-6 py-3 bg-gradient-to-r from-blue-700 to-blue-500 text-white
                font-semibold rounded-lg shadow-md hover:from-blue-600 hover:to-blue-400
                hover:scale-105 transition-transform duration-200 border-2 border-blue-800`}
        >
            {children}
        </button>
    );
}

function EncounterButton({ onClick, type = 'button', children }) {
    return (
        <button 
            type={type} 
            onClick={onClick} 
            className={`min-w-20 px-6 py-3 bg-gradient-to-r from-green-700 to-green-500 text-white
                font-semibold rounded-lg shadow-md hover:from-green-600 hover:to-green-400
                hover:scale-105 transition-transform duration-200 border-2 border-green-800`}
        >
            {children}
        </button>
    );
}

export { MysticButton, EncounterButton };