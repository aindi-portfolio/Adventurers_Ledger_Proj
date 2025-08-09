export default function InputField({ type = 'text', name = '', placeholder, className = '' }) {
    return (
        <input
            type={type}
            name={name}
            placeholder={placeholder}
            className={`min-w-4/12 px-4 py-2 bg-gray-100 border-2 border-yellow-800 rounded-lg
                shadow-sm focus:ring-2 focus:ring-yellow-500 forcus:border-yellow-600 transition
                duration-200 ${className}`}
        />
    );
}