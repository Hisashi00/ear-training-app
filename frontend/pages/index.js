import { useRouter } from "next/router";

export default function Home() {
  const router = useRouter();

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <h1 className="text-3xl font-bold mb-6">Ear Training App</h1>
      <button
        className="px-4 py-2 bg-blue-500 text-white rounded mb-4"
        onClick={() => router.push("/practice")}
      >
        Practice Mode
      </button>
      <button
        className="px-4 py-2 bg-green-500 text-white rounded"
        onClick={() => router.push("/test")}
      >
        Test Mode
      </button>
    </div>
  );
}
